from django.conf import settings
from django.db import models


class Events1(models.Model):
    "Generated Model"
    address1 = models.CharField(
        max_length=256,
    )
    address2 = models.CharField(
        max_length=256,
    )
    city = models.CharField(
        max_length=256,
    )


class Events(models.Model):
    "Generated Model"
    event_name = models.DateField()
    event_description = models.CharField(
        max_length=256,
    )
    event_location = models.ForeignKey(
        "events.Events1",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="events_event_location",
    )


# Create your models here.
