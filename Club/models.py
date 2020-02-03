from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingTitle=models.CharField(max_length=255)
    meetingDate=models.DateField()
    meetingTime=models.TimeField()
    meetingLocation=models.CharField(max_length=255)
    meetingAgenda=models.TextField()
    
    class Meta:
        db_table='meeting'
        verbose_name_plural='meeting'
        
class MeetingMinutes(models.Model):
    meetingID=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendence=models.IntegerField()
    minutesText=models.TextField()
    
    class Meta:
        db_table='meetingMinutes'
        verbose_name_plural='meetingMinutes'


class Resource(models.Model):
    resourceName=models.CharField(max_length=255)
    resourceType=models.CharField(max_length=255)
    resourceURL=models.URLField()
    dateEntered=models.DateField()
    userID=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField()
    resourceManager = models.Manager()
    
    def __str__(self):
        return self.resourceName
    class Meta:
        db_table='resource'
        verbose_name_plural='resource'

class Event(models.Model):
    eventTitle=models.CharField(max_length=255)
    eventLocation=models.CharField(max_length=255)
    eventDate=models.DateField()
    eventTime=models.TimeField()
    description=models.TextField()
    userId=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table='event'
        verbose_name_plural='event'