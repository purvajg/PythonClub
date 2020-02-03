from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'clubApp/index.html')

def getResources(request):
    resource_list= Resource.resourceManager.all()
    return render(request, 'clubApp/resource.html', {'resource_list' : resource_list})
