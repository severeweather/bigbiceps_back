from ..models import FoodCuisine
from ..exeptions import IDNotFound, AlreadyExists
from django.db import IntegrityError


class FoodCuisineRepository:
    @staticmethod
    def get_all():
        return [
            {"id": x.id, "name": x.name} for x in FoodCuisine.objects.all()
        ]

    @staticmethod
    def get_by_id(id):
        try:
            return FoodCuisine.objects.get(id=id)
        except FoodCuisine.DoesNotExist:
            raise IDNotFound(FoodCuisine, id)

    @staticmethod
    def create(name):
        try:
            FoodCuisine.objects.create(name=name)
        except IntegrityError:
            raise AlreadyExists()