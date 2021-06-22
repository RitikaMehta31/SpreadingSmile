from django.forms import ModelForm,Textarea
from django import forms
from .models import VolunteerModel

class VolunteerForm(ModelForm):

	q3=forms.CharField(required=True,label='Why do you want to volunteer?',widget=forms.Textarea(
		attrs={
    	'rows': 5
    	}))

	class Meta:
		model=VolunteerModel
		fields=['fullname','mobile','image','q2','q1','q3']
		widgets={'q1':forms.RadioSelect,'q2':forms.RadioSelect}
		labels={'q1':'What time can you work?','q2':'Are you a Student?','image':'Your Picture (Recommneded size: 512px X 512px)'}