from django.http import JsonResponse
from django.views import View
from app.models import CalendarEvent


class DeleteEvent(View):
    def post(self, request):
        event_id = request.POST.get("event_id")
        try:
            event = CalendarEvent.objects.get(id=event_id)
            event.delete()
            return JsonResponse({"success": True})
        except CalendarEvent.DoesNotExist:
            return JsonResponse({"success": False, "error": "Event not found"})

    def get(self, request):
        return JsonResponse({"success": False, "error": "Invalid request method"})
