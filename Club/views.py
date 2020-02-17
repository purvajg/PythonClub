from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'clubApp/index.html')

def getResources(request):
    resource_list= Resource.resourceManager.all()
    return render(request, 'clubApp/resource.html', {'resource_list' : resource_list})

def getMeetings(request):
    meeting_list= Meeting.meetingManager.all()
    # meeting_list=Meeting.objects.all()
    return render(request, 'clubApp/meetings.html', {'meeting_list' : meeting_list})

def getMeetingDetails(request, id):
    meetingWithThatId=get_object_or_404(MeetingMinutes, meetingId=id)
    print ("Meeting with id ", meetingWithThatId)
    # meetingWithThatId=Meeting.meetingManager.meetingid(id)
    return render(request, 'clubApp/details.html', {'meetingWithThatId' : meetingWithThatId})
    