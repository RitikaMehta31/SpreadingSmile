from django.shortcuts import render,redirect,get_object_or_404
from .models import VolunteerModel,MemberModel
from .forms import VolunteerForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def volunteerform(request):
	if request.method=='GET':
		form=VolunteerForm()
		context={'form':form}
		template='volunteer.html'
		return render(request,template,context)
	else:
		form=VolunteerForm(request.POST,request.FILES or None)
		newform=form.save(commit=False)
		newform.user=request.user
		newform.email=request.user.email			
		newform.save()
		return redirect('home')

@login_required
def registeredvolunteers(request):
	if request.user.has_perm('poll.change_poll'):
		admin=True
		volunteers=VolunteerModel.objects.all()
		context={'admin':admin,'volunteers':volunteers}
		template='allvolunteers.html'
		return render(request,template,context)
	else:
		return redirect('home')


def acceptvolunteer(request, volunteer_pk):
	if request.user.has_perm('poll.change_poll'):
		admin=True
		volunteer=VolunteerModel.objects.get(pk=volunteer_pk)
		member=MemberModel.objects.create(name=volunteer.fullname)
		member.image=volunteer.image
		member.positon="Volunteer"
		member.save()
		volunteer.delete()
		return redirect('volunteers')
	else:
		return redirect('home')

def rejectvolunteer(request, volunteer_pk):
	if request.user.has_perm('poll.change_poll'):
		admin=True
		volunteer=VolunteerModel.objects.get(pk=volunteer_pk)
		volunteer.delete()
		return redirect('volunteers')
	else:
		return redirect('home')