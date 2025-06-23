from ..models import FoodItemCategory
from django.db import IntegrityError
from ..exeptions import AlreadyExists
from .utils import FoodItemRelationChecker


class FoodItemCategoryRepository:
    @staticmethod
    def create(food_item, category):
        try:
            FoodItemCategory.objects.create(food=food_item, category=category)
        except IntegrityError:
            raise AlreadyExists()
        
    @staticmethod
    def exists(id):
        return FoodItemRelationChecker.exists(FoodItemCategory, id)