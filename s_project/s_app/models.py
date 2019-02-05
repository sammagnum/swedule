import uuid

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import pytz
from timezone_field import TimeZoneField
# Create your models here.


def get_new_teamlead():
    return "fix this later"


class Request(models.Model):
    """Model representing a timeoff request."""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_time = models.DateTimeField
    swe_email = models.ForeignKey("Swe", on_delete=models.DO_NOTHING)

    TYPE = (
        ('v', 'Vacation'),
        ('f', 'Floating Holiday'),
        ('i', 'Ill/Sick'),
        ('p', 'Personal'),
    )

    TYPE = models.CharField(
        max_length=1,
        choices=TYPE,
        blank=False,
        default='v',
        help_text='Reason for Time-Off Request',
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.request_uuid

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[self.request_uuid])


class Teamlead(models.Model):
    user_email = models.OneToOneField(User, on_delete=models.DO_NOTHING, primary_key=True)

    def __str__(self):
        """String for representing the Model object."""
        return str(self.user_email)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.user_email)])


class Team(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    lead = models.ForeignKey("Teamlead", on_delete=models.DO_NOTHING)

    def __str__(self):
        """String for representing the Model object."""
        return str(self.name)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=str([self.name]))


class Manager(models.Model):
    user_email = models.OneToOneField(User, on_delete=models.DO_NOTHING, primary_key=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.user_email

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.user_email)])


class Swe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    team = models.ForeignKey("Team", on_delete=models.DO_NOTHING)
    timezone = TimeZoneField(default="US/Eastern")


    def __str__(self):
        """String for representing the Model object."""
        return str(self.user.id)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.user)])


class Event(models.Model):
    event_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    swe = models.ForeignKey("Swe", on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ["start_time"]

    TYPE = (
        ('s', 'Shift'),
        ('m', 'Meeting'),
        ('v', 'Vacation'),
        ('f', 'Floating Holiday'),
        ('i', 'Ill/Sick'),
        ('p', 'Personal'),
    )

    type = models.CharField(
        max_length=1,
        choices=TYPE,
        blank=False,
        default='s',
        help_text='Type of Event',
    )

    def __str__(self):
        """String for representing the Model object."""
        return "start: " + str(self.start_time) + " end: " + str(self.end_time)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[self.event_uuid])
