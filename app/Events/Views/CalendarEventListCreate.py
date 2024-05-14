from rest_framework import generics
from app.models import CalendarEvent
from app.serializers import CalendarEventSerializer
from rest_framework.response import Response


class CalendarEventListCreate(generics.ListCreateAPIView):
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventSerializer
