from django.shortcuts import render,redirect
from .models import DonationModel,UserRewardModel
from volunteers.models import VolunteerModel,MemberModel
from .forms import DonationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
	if request.user.is_authenticated:
		userrewar,created=UserRewardModel.objects.get_or_create(user=request.user)
		request.session['reward']=userrewar.points
		if VolunteerModel.objects.filter(user=request.user).exists():
			volunteerReg=True
		else:
			volunteerReg=False
		if request.user.has_perm('poll.change_poll'):
			admin=True
		else:
			admin=False
		
	else:
		volunteerReg=False
		admin=False

	founder=MemberModel.objects.filter(position='Founder').first()
	members=MemberModel.objects.filter(position='Volunteer')
	context={'volunteerReg':volunteerReg,'members':members,'founder':founder,'admin':admin}
	template='home.html'
	return render(request,template,context)

@login_required
def donation(request):
	request.session.set_expiry(120000)
	if request.method=='GET':
		form=DonationForm()
		context={'form':form}
		template='donationform.html'
		return render(request,template,context)
	else:
		form=DonationForm(request.POST or None)
		newform=form.save(commit=False)
		newform.user=request.user
		userrewar,created=UserRewardModel.objects.get_or_create(user=request.user)
		userrewar.points+=10
		request.session['reward']=userrewar.points
		userrewar.save()
		newform.save()
		return redirect('home')