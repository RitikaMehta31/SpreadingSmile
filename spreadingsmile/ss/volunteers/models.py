from django.db import models

from django.contrib.auth import get_user_model

User=get_user_model()

q1_choice=(
	('9 - 12','9 - 12'),
	('1 - 5','1 - 5'),
	('Any Time','Any Time'),
)

q2_choice=(
	('Yes','Yes'),
	('No','No'),
)

position_choice=(
	('Founder','Founder'),
	('Volunteer','Volunteer'),
	)
# Create your models here.
class VolunteerModel(models.Model):
	fullname=models.CharField(default="",max_length=100)
	mobile=models.IntegerField(default=0)
	image=models.ImageField(blank=True,null=True,upload_to='volunteers')
	q1=models.CharField(max_length=100,choices=q1_choice,default='9 - 12')
	q2=models.CharField(max_length=100,choices=q2_choice,default='Yes')
	q3=models.TextField(default="")
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	email=models.EmailField(default="")

	def __str__(self):
		return self.fullname

class MemberModel(models.Model):
	name=models.CharField(default="",max_length=100)
	position=models.CharField(default="Volunteer",max_length=100,choices=position_choice)
	image=models.ImageField(blank=True,null=True,upload_to='members')

	def __str__(self):
		return self.name