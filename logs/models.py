from django.db import models
import uuid


class MealLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    foods = models.JSONField(default=dict)
    logged = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


# class ProgressLog(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     activity_level = models.CharField(max_length=15, choices=ACTIVITY_LEVEL_CHOICES, default='sed')
#     goal = models.CharField(max_length=15, choices=GOAL_CHOICES, default='mainw')
#     meal_logs = models.JSONField(default=dict)
#     target_cals = models.DecimalField(max_digits=5, decimal_places=1, default=0)
#     target_carbs = models.DecimalField(max_digits=5, decimal_places=1, default=0)
#     target_prot = models.DecimalField(max_digits=5, decimal_places=1, default=0)
#     target_fats = models.DecimalField(max_digits=5, decimal_places=1, default=0)
#     real_cals = models.DecimalField(max_digits=5, decimal_places=1, default=0)
#     real_carbs = models.DecimalField(max_digits=5, decimal_places=1, default=0)
#     real_prot = models.DecimalField(max_digits=5, decimal_places=1, default=0)
#     real_fats = models.DecimalField(max_digits=5, decimal_places=1, default=0)
#     logged_weight = models.DecimalField(max_digits=4, decimal_places=1, null=True)
#     approx_delta_weight = models.DecimalField(max_digits=4, decimal_places=1, default=0)
#     approx_delta_fat = models.DecimalField(max_digits=4, decimal_places=1, default=0)
#     approx_delta_muscle = models.DecimalField(max_digits=4, decimal_places=1, default=0)
#     logged = models.DateField(auto_now_add=True)
#     updated = models.DateField(auto_now=True)