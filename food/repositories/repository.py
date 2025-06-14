from django.db import IntegrityError

from ..models import *
from ..exceptions.exeptions import IDNotFound, AlreadyExists


class FoodItemRelationChecker:
    @staticmethod
    def exists(model, food_item_id):
        try:
            food_item = FoodItem.objects.get(id=food_item_id)
            return model.objects.filter(food=food_item).exists()
        except FoodItem.DoesNotExist:
            raise IDNotFound(FoodItem, food_item_id)
        


class NutrientRepository:
    model = Nutrient

    @staticmethod
    def get_all():
        model = NutrientRepository.model
        return [
            {"id": x.id, "name": x.name, "unit": x.unit} for x in model.objects.all()
        ]

    @staticmethod
    def get_by_id(id):
        model = NutrientRepository.model

        try:
            return model.objects.get(id=id)
        except model.DoesNotExist:
            raise IDNotFound(model, id)

    @staticmethod
    def create(name, unit):
        model = NutrientRepository.model

        try:
            model.objects.create(name=name, unit=unit)
        except IntegrityError:
            raise AlreadyExists    


class FoodCategoryRepository:
    model = FoodCategory

    @staticmethod
    def get_all():
        model = FoodCategoryRepository.model
        return [
            {"id": x.id, "name": x.name} for x in model.objects.all()
        ]
    
    @staticmethod
    def get_by_id(id):
        model = FoodCategoryRepository.model

        try:
            return model.objects.get(id=id)
        except model.DoesNotExist:
            raise IDNotFound(model, id)

    @staticmethod
    def create(name):
        model = FoodCategoryRepository.model

        try:
            model.objects.create(name=name)
        except IntegrityError:
            raise AlreadyExists

    @staticmethod
    def patch():
        pass

    @staticmethod
    def delete():
        pass


class FoodCuisineRepository:
    model = FoodCuisine

    @staticmethod
    def get_all():
        model = FoodCuisineRepository.model
        return [
            {"id": x.id, "name": x.name} for x in model.objects.all()
        ]

    @staticmethod
    def get_by_id(id):
        model = FoodCuisineRepository.model

        try:
            return model.objects.get(id=id)
        except model.DoesNotExist:
            raise IDNotFound(model, id)

    @staticmethod
    def create(name):
        model = FoodCuisineRepository.model

        try:
            model.objects.create(name=name)
        except IntegrityError:
            raise AlreadyExists

    @staticmethod
    def patch():
        pass

    @staticmethod
    def delete():
        pass



class FoodItemRepository:
    model = FoodItem

    @staticmethod
    def get_by_id(id):
        model = FoodItemRepository.model
        try:
            return model.objects.get(id=id)
        except model.DoesNotExist:
            raise IDNotFound(model, id)
        
    @staticmethod
    def get_all(food_type=None):
        if food_type not in ("ingredient", "dish", "meal"):
            return []
        
        return [
            {
                "id": x.id, 
                "type": x.type, 
                "name": x.name, 
                "description": x.description, 
                "recipe": x.recipe,
                "is_public": x.is_public,
                "created": x.created,
                "created_by": x.created_by.id
            } 
            for x in FoodItem.objects.filter(type=food_type)
        ]

class FoodItemNutrientRepository:
    model = FoodItemNutrient
    
    @staticmethod
    def get_by_id(id):
        model = FoodItemNutrientRepository.model
        try:
            return model.objects.get(id=id)
        except model.DoesNotExist:
            raise IDNotFound(model, id)

    @staticmethod
    def create(food_item, nutrient, amount):
        model = FoodItemNutrientRepository.model
        try:
            model.objects.create(food=food_item, nutrient=nutrient, amount=amount)
        except IntegrityError:
            raise AlreadyExists
        
    @staticmethod
    def exists(id):
        model = FoodItemNutrientRepository.model
        return FoodItemRelationChecker.exists(model, id)


class FoodItemCategoryRepository:
    model = FoodItemCategory

    @staticmethod
    def create(food_item, category):
        model = FoodItemCategoryRepository.model
        try:
            model.objects.create(food=food_item, category=category)
        except IntegrityError:
            raise AlreadyExists
        
    @staticmethod
    def exists(id):
        model = FoodItemCategoryRepository.model
        return FoodItemRelationChecker.exists(model, id)


class FoodItemCuisineRepository:
    model = FoodItemCuisine

    @staticmethod
    def create(food_item, cuisine):
        model = FoodItemCuisineRepository.model
        try:
            model.objects.create(food=food_item, cuisine=cuisine)
        except IntegrityError:
            raise AlreadyExists
        
    @staticmethod
    def exists(id):
        model = FoodItemCuisineRepository.model
        return FoodItemRelationChecker.exists(model, id)


class FoodItemChildRepository:
    model = FoodItemChild

    @staticmethod
    def add(parent, child, amount):
        model = FoodItemChildRepository.model

        model.objects.create(parent=parent, child=child, amount=amount)
        return

