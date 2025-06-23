from ..models import FoodItemNutrient
from .food_item_repository import FoodItemRepository
from ..exeptions import IDNotFound, AlreadyExists
from django.db import IntegrityError
from .utils import FoodItemRelationChecker


class FoodItemNutrientRepository:
    @staticmethod
    def get_by_id(id):
        try:
            return FoodItemNutrient.objects.get(id=id)
        except FoodItemNutrient.DoesNotExist:
            raise IDNotFound(FoodItemNutrient, id)

    @staticmethod
    def get_food_item_nutrients(id):
        try:
            food_item = FoodItemRepository.get_by_id(id)
            return {str(x.nutrient.id): x.amount for x in FoodItemNutrient.objects.filter(food=food_item)}
        except FoodItemNutrient.DoesNotExist:
            raise IDNotFound(FoodItemNutrient, id)

    @staticmethod
    def create(food_item, nutrient, amount):
        try:
            FoodItemNutrient.objects.create(food=food_item, nutrient=nutrient, amount=amount)
        except IntegrityError:
            raise AlreadyExists()
        
    @staticmethod
    def exists(id):
        return FoodItemRelationChecker.exists(FoodItemNutrient, id)