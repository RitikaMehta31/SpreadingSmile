from django.contrib import admin
from .models import UserRewardModel,DonationModel
# Register your models here.
admin.site.register(UserRewardModel)
admin.site.register(DonationModel)
