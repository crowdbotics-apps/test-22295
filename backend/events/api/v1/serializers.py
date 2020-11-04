from rest_framework import serializers
from events.models import Events, Events1


class Events1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Events1
        fields = "__all__"


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"
