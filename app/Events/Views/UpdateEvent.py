from django.http import JsonResponse
from django.views import View
from django.utils.dateparse import parse_datetime
from app.models import CalendarEvent


class UpdateEvent(View):
    def post(self, request):
        if request.method == "POST":
            event_id = request.POST.get("event_id")
            title = request.POST.get("title")
            start_date_str = request.POST.get("start")
            end_date_str = request.POST.get("end")
            all_day_str = request.POST.get("allDay")

            # Parse the datetime strings into datetime objects
            start_date = parse_datetime(start_date_str)
            end_date = parse_datetime(end_date_str) if end_date_str else None

            # Convert 'true' and 'false' strings to boolean values
            all_day = all_day_str.lower() == "true"

            try:
                event = CalendarEvent.objects.get(id=event_id)
                event.title = title
                event.start_date = start_date

                # Debug output
                print("Original End Date:", event.end_date)
                print("Start Date:", start_date)
                print("End Date:", end_date)
                print("All Day:", all_day)

                event.end_date = end_date
                event.all_day = all_day
                event.save()

                return JsonResponse({"success": True})
            except CalendarEvent.DoesNotExist:
                return JsonResponse({"success": False, "error": "Event not found"})
        return JsonResponse({"success": False, "error": "Invalid request method"})
