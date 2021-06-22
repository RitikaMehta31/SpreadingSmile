from django.db import models

# Create your models here.
class EventModel(models.Model):
	name=models.CharField(max_length=100)
	description=models.TextField()
	date=models.DateField(null=True)

	def __str__(self):
		return self.name