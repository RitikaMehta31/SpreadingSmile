from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EventModel
# Create your views here.
def upcomingevents(request):
	events=EventModel.objects.all()
	context={'events':events}
	template='upcoming.html'
	return render(request,template,context)

def detail(request,event_pk):
	event=get_object_or_404(EventModel, pk=event_pk)
	context={'event':event}
	template='detail.html'
	return render(request,template,context)
