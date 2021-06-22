from django.forms import ModelForm,Textarea
from django import forms
from .models import DonationModel


class DonationForm(ModelForm):
	
	address=forms.CharField(required=True,widget=forms.Textarea(
		attrs={
    	'rows': 5,
    	}))

	
	class Meta:
		model=DonationModel
		fields=['name','address','city','date','mobile','categories']
		widget={'categories':forms.CheckboxSelectMultiple}
		
