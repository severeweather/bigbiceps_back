from django.db import models
from accounts.models import CustomUser
import uuid


class FoodItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(null=False)
    name = models.CharField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    recipe = models.TextField(null=True, blank=True)

    is_public = models.BooleanField(default=False) 
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class FoodCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True)


class FoodCuisine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True)


class FoodItemCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("food", "category")
    
    
class FoodItemCuisine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(FoodCuisine, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("food", "cuisine")


class Nutrient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False)
    unit = models.CharField(blank=False)

    class Meta:
        unique_together = ("name", "unit")
    
    
class FoodItemNutrient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)

    class Meta:
        unique_together = ('food', 'nutrient')


class FoodItemComposition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name="parent")
    child = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name="child")
    amount = models.IntegerField(null=False, blank=False)

    class Meta:
        unique_together = ('parent', 'child')