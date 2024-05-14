from rest_framework import serializers, pagination
from .models import ClientModel

# Serializer for the ClientModel
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = "__all__"


# Custom pagination class
class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


# DRF view for the ClientModel
from rest_framework.generics import ListAPIView

from app.models import CalendarEvent


class CalendarEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarEvent
        fields = "__all__"


class ClientModelListView(ListAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer
    pagination_class = CustomPagination
