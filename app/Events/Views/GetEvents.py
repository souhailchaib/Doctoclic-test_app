from django.http import JsonResponse
from django.views.generic import CreateView

from app.models import CalendarEvent


class GetEvents(CreateView):
    def get(self, request):
        events = CalendarEvent.objects.all()
        event_data = []
        for event in events:
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
