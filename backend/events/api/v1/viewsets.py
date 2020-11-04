from rest_framework import authentication
from events.models import Events, Events1
from .serializers import EventsSerializer, Events1Serializer
from rest_framework import viewsets


class Events1ViewSet(viewsets.ModelViewSet):
    serializer_class = Events1Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Events1.objects.all()


class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Events.objects.all()
