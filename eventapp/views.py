from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .forms import Participantform

# Create your views here.

def index(request):
    events = Event.objects.all()   #take all objects ie events (all data in event table in DB)
    context = {
        'events' : events
    }
    return render(request,'eventapp/index.html',context)

def eventdetail(request,pk):
    events=Event.objects.all()
    for event in events:
        if event.pk==pk:
            req_event=event
    if request.method == 'POST':
        form=Participantform(request.POST)
        if form.is_valid():
            participant=form.save(commit=False)
            participant.event = req_event
            participant.save()
    
    form=Participantform()
    context={
         'event' : req_event,
         'form' : form
    }
    return render(request,'eventapp/details.html',context)
