from ..models import Nutrient
from food.serializers.nutrient_serializer import NutrientSerializer
from ..exeptions import IDNotFound, AlreadyExists
from django.db import IntegrityError


class NutrientRepository:
    @staticmethod
    def get_all():
        return [
            NutrientSerializer.to_dict(x) for x in Nutrient.objects.all()
        ]
    
    @staticmethod
    def get_all_dict():
        return {str(x.id): str(x.name) for x in Nutrient.objects.all()}

    @staticmethod
    def get_by_id(id):
        try:
            return Nutrient.objects.get(id=id)
        except Nutrient.DoesNotExist:
            raise IDNotFound(Nutrient, id)

    @staticmethod
    def create(name, unit):
        try:
            Nutrient.objects.create(name=name, unit=unit)
        except IntegrityError:
            raise AlreadyExists() 