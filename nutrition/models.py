from django.db import models

from src.common import ACTIVITY_LEVEL_CHOICES, SEX_CHOICES

class UserNutritionProfile(models.Model):
    owner = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE)
    wght = models.FloatField(default=0)
    hght = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    sex = models.CharField(choices=SEX_CHOICES, default="na")
    act_lvl = models.CharField(choices=ACTIVITY_LEVEL_CHOICES, default="na")
    lbm = models.FloatField(default=0)
    bmr = models.FloatField(default=0)
    tdee = models.FloatField(default=0)

    goal_cal = models.FloatField(default=0)
    goal_car = models.FloatField(default=0)
    goal_pro = models.FloatField(default=0)
    goal_fat= models.FloatField(default=0)

