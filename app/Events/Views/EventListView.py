from django.http import JsonResponse


from django.views.generic import View

from app.models import CalendarEvent


class EventListView(View):

    model = CalendarEvent

    def render_to_response(self, context, **response_kwargs):
        event_data = []
        for event in context["object_list"]:
            event_data.append(
                {
                    "id": event.id,
                    "title": event.title,
                    "start": event.start_date.isoformat(),
                    "end": event.end_date.isoformat() if event.end_date else None,
                    "allDay": event.all_day,
                }
            )
        return JsonResponse(event_data, safe=False)
