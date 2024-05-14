from django.http import JsonResponse
from django.views import View
from app.models import CalendarEvent


class GetEvent(View):
    def get(self, request):
        event_id = request.GET.get("event_id")

        # Fetch the event details from the database
        try:
            event = CalendarEvent.objects.get(id=event_id)
            event_data = {
                "title": event.title,
                "start": event.start_date.isoformat(),
                "end": event.end_date.isoformat() if event.end_date else None,
                "allDay": event.all_day,
            }
            return JsonResponse({"event_data": event_data})

        except CalendarEvent.DoesNotExist:
            return JsonResponse({"error": "Event not found"}, status=404)

    def post(self, request):
        return JsonResponse({"error": "Invalid request method"}, status=405)
