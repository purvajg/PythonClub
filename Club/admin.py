from django.contrib import admin
from .models import MeetingMinutes, Meeting, Resource, Event

# Register your models here.
admin.site.register(MeetingMinutes)
admin.site.register(Meeting)
admin.site.register(Resource)
admin.site.register(Event)