from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, ResourceForm

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
    
def newMeeting(request):
    form= MeetingForm
    if request.method=='POST':
        form= MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'clubApp/newMeeting.html', {'form':form})

def newResource(request):
    form= ResourceForm
    if request.method=='POST':
        form= ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'clubApp/newResource.html', {'form':form})