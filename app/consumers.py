from channels.generic.websocket import AsyncWebsocketConsumer

from .tasks import send_email_task
from .models import CalendarEvent, ClientModel, MedecinModel
from asgiref.sync import sync_to_async
import json
import datetime

create_event_async = sync_to_async(CalendarEvent.objects.create)

class EventConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("calendar", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("calendar", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        print (text_data)
        print (data)
        action = data.get("action")

        if action == "event_created":
            await self.create_event(data["data"])
        elif action == "event_updated":
            await self.update_event(data["data"])
        elif action == "event_deleted":
            await self.delete_event(data["data"])

    async def create_event(self, data):
        
        title = data.get("title")
        start = data.get("start")
        end = (
            datetime.datetime.strptime(data.get("end", ""), "%Y-%m-%dT%H:%M:%S.%fZ")
            if data.get("end")
            else None
        )
        all_day = data.get("allDay")
        medecin_id = data.get("medecin_id")
        client_id = data.get("client_id")
        try:
            client = await sync_to_async(ClientModel.objects.get)(id=client_id)
            medecin = await sync_to_async(MedecinModel.objects.get)(id=medecin_id)
            event = await create_event_async(
                client=client,title=title, start_date=start, end_date=end, all_day=all_day , medecin=medecin
            )
            event_data = {
                "client_id": client_id,  # Include client_id in the event data
                "id": event.id,
                "title": event.title,
                "start": event.start_date,
                "end": event.end_date if event.end_date else None,
                "allDay": event.all_day,
                "medecin_id": medecin_id,
            }

            print (event_data)
            await self.channel_layer.group_send(
                "calendar",
                {
                    "type": "event_message",
                    "message": {
                        "action": "event_created",
                        "data": event_data,
                        "message": "Event created successfully.",
                    },
                },
            )
            # send_email_task.delay()
        except (ClientModel.DoesNotExist, MedecinModel.DoesNotExist) as e:
            await self.send(text_data=json.dumps({"error": str(e)}))

    async def update_event(self, data):
        # Extract event data from the payload
        event_id = data.get("id")
        title = data.get("title")
        start = data.get("start")
        end = data.get("end")
        all_day = data.get("allDay")

        # Retrieve the CalendarEvent object from the database
        try:
            event = await sync_to_async(CalendarEvent.objects.get)(id=event_id)

            # Update the fields and save the object
            event.title = title
            event.start_date = start
            event.end_date = end
            event.all_day = all_day
            await sync_to_async(event.save)()

            # Send a response back to the client if needed
            await self.send(
                text_data=json.dumps({"message": "Event updated successfully."})
            )

            # Notify the group about the updated event
            await self.channel_layer.group_send(
                "calendar",
                {
                    "type": "event_message",
                    "message": {
                        "action": "event_updated",
                        "data": data,
                        "message": "Event updated successfully.",
                    },
                },
            )
        except CalendarEvent.DoesNotExist:
            await self.send(text_data=json.dumps({"error": "Event not found."}))

    async def delete_event(self, data):
        # Extract event ID from the payload
        event_id = data.get("id")

        # Retrieve the CalendarEvent object from the database and delete it
        try:
            event = await sync_to_async(CalendarEvent.objects.get)(id=event_id)
            await sync_to_async(event.delete)()

            # Send a response back to the client if needed
            await self.send(
                text_data=json.dumps({"message": "Event deleted successfully."})
            )

            # Notify the group about the deleted event
            await self.channel_layer.group_send(
                "calendar",
                {
                    "type": "event_message",
                    "message": {
                        "action": "event_deleted",
                        "data": data,
                        "message": "Event deleted successfully.",
                    },
                },
            )
        except CalendarEvent.DoesNotExist:
            await self.send(text_data=json.dumps({"error": "Event not found."}))

    async def event_message(self, event):
        # Send the event message to the group
        await self.send(text_data=json.dumps(event))
