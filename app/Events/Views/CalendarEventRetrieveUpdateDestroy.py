from rest_framework import generics
from app.models import CalendarEvent
from app.serializers import CalendarEventSerializer


class CalendarEventRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventSerializer
