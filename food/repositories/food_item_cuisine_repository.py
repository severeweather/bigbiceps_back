from ..models import FoodItemCuisine
from django.db import IntegrityError
from ..exeptions import AlreadyExists
from .utils import FoodItemRelationChecker


class FoodItemCuisineRepository:
    @staticmethod
    def create(food_item, cuisine):
        try:
            FoodItemCuisine.objects.create(food=food_item, cuisine=cuisine)
        except IntegrityError:
            raise AlreadyExists()
        
    @staticmethod
    def exists(id):
        return FoodItemRelationChecker.exists(FoodItemCuisine, id)