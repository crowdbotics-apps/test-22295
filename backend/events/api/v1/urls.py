from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import EventsViewSet, Events1ViewSet

router = DefaultRouter()
router.register("events1", Events1ViewSet)
router.register("events", EventsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
