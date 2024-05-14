from django.http import JsonResponse
from django.views import View
from django.utils.dateparse import parse_datetime
from app.models import CalendarEvent


class SaveEvent(View):
    def post(self, request):
        if request.method == "POST":
            title = request.POST.get("title")
            start_date_str = request.POST.get("start")
            end_date_str = request.POST.get("end")
            all_day_str = request.POST.get("allDay")

            # Parse the datetime strings into datetime objects
            start_date = parse_datetime(start_date_str)
            end_date = parse_datetime(end_date_str) if end_date_str else None

            # Convert 'true' and 'false' strings to boolean values
            all_day = all_day_str.lower() == "true"

            # Create a new event
            new_event = CalendarEvent.objects.create(
                title=title, start_date=start_date, end_date=end_date, all_day=all_day
            )

            # Return the ID of the newly created event in the response
            return JsonResponse({"success": True, "event_id": new_event.id})
        else:
            return JsonResponse({"success": False, "error": "Invalid request method"})
