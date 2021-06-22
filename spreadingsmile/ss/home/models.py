from django.db import models
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField

User=get_user_model()

donation_choice=(
    ("clothes","Clothes"),
    ("books","Books"),
    ("toys","Toys"),
    ("educate_kids","Educate Kids")
    )


# Create your models here.
class UserRewardModel(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	points=models.IntegerField(default=0)

	def __str__(self):
		return str(self.user)

class DonationModel(models.Model):
	name=models.CharField(default="",max_length=100)
	address=models.TextField(default="")
	city=models.CharField(default="",max_length=100)
	date=models.DateTimeField(null=True)
	mobile=models.IntegerField(default=0)
	categories=MultiSelectField(default=" ",choices=donation_choice,max_length=100)
	user=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.name