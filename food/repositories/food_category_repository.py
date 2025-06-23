from ..models import FoodCategory
from ..exeptions import IDNotFound, AlreadyExists
from django.db import IntegrityError


class FoodCategoryRepository:
    @staticmethod
    def get_all():
        return [
            {"id": x.id, "name": x.name} for x in FoodCategory.objects.all()
        ]
    
    @staticmethod
    def get_by_id(id):
        try:
            return FoodCategory.objects.get(id=id)
        except FoodCategory.DoesNotExist:
            raise IDNotFound(FoodCategory, id)

    @staticmethod
    def create(name):
        try:
            FoodCategory.objects.create(name=name)
        except IntegrityError:
            raise AlreadyExists()