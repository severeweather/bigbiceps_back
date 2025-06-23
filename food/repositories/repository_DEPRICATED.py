# from django.db import IntegrityError

# from ..models import *
# from ..serializers import *
# from ..exeptions import IDNotFound, AlreadyExists


# class FoodItemRelationChecker:
#     @staticmethod
#     def exists(model, food_item_id):
#         try:
#             food_item = FoodItem.objects.get(id=food_item_id)
#             return model.objects.filter(food=food_item).exists()
#         except FoodItem.DoesNotExist:
#             raise IDNotFound(FoodItem, food_item_id)
        

# class NutrientRepository:
#     @staticmethod
#     def get_all():
#         return [
#             NutrientSerializer.to_dict(x) for x in Nutrient.objects.all()
#         ]
    
#     @staticmethod
#     def get_all_dict():
#         return {str(x.id): str(x.name) for x in Nutrient.objects.all()}

#     @staticmethod
#     def get_by_id(id):
#         try:
#             return Nutrient.objects.get(id=id)
#         except Nutrient.DoesNotExist:
#             raise IDNotFound(Nutrient, id)

#     @staticmethod
#     def create(name, unit):
#         try:
#             Nutrient.objects.create(name=name, unit=unit)
#         except IntegrityError:
#             raise AlreadyExists() 


# class FoodCategoryRepository:
#     @staticmethod
#     def get_all():
#         return [
#             {"id": x.id, "name": x.name} for x in FoodCategory.objects.all()
#         ]
    
#     @staticmethod
#     def get_by_id(id):
#         try:
#             return FoodCategory.objects.get(id=id)
#         except FoodCategory.DoesNotExist:
#             raise IDNotFound(FoodCategory, id)

#     @staticmethod
#     def create(name):
#         try:
#             FoodCategory.objects.create(name=name)
#         except IntegrityError:
#             raise AlreadyExists()


# class FoodCuisineRepository:
#     @staticmethod
#     def get_all():
#         return [
#             {"id": x.id, "name": x.name} for x in FoodCuisine.objects.all()
#         ]

#     @staticmethod
#     def get_by_id(id):
#         try:
#             return FoodCuisine.objects.get(id=id)
#         except FoodCuisine.DoesNotExist:
#             raise IDNotFound(FoodCuisine, id)

#     @staticmethod
#     def create(name):
#         try:
#             FoodCuisine.objects.create(name=name)
#         except IntegrityError:
#             raise AlreadyExists()


# class FoodItemRepository:
#     @staticmethod
#     def get_by_id(id):
#         try:
#             return FoodItem.objects.get(id=id)
#         except FoodItem.DoesNotExist:
#             raise IDNotFound(FoodItem, id)
        
#     @staticmethod
#     def get_all(food_type=None):
#         if food_type not in ("ingredient", "dish", "meal"):
#             return []
        
#         return [
#             {
#                 "id": x.id, 
#                 "type": x.type, 
#                 "name": x.name, 
#                 "description": x.description, 
#                 "recipe": x.recipe,
#                 "is_public": x.is_public,
#                 "created": x.created,
#                 "created_by": x.created_by.id
#             } 
#             for x in FoodItem.objects.filter(type=food_type)
#         ]


# class FoodItemNutrientRepository:
#     @staticmethod
#     def get_by_id(id):
#         try:
#             return FoodItemNutrient.objects.get(id=id)
#         except FoodItemNutrient.DoesNotExist:
#             raise IDNotFound(FoodItemNutrient, id)

#     @staticmethod
#     def get_food_item_nutrients(id):
#         try:
#             food_item = FoodItemRepository.get_by_id(id)
#             return {str(x.nutrient.id): x.amount for x in FoodItemNutrient.objects.filter(food=food_item)}
#         except FoodItemNutrient.DoesNotExist:
#             raise IDNotFound(FoodItemNutrient, id)

#     @staticmethod
#     def create(food_item, nutrient, amount):
#         try:
#             FoodItemNutrient.objects.create(food=food_item, nutrient=nutrient, amount=amount)
#         except IntegrityError:
#             raise AlreadyExists()
        
#     @staticmethod
#     def exists(id):
#         return FoodItemRelationChecker.exists(FoodItemNutrient, id)


# class FoodItemCategoryRepository:
#     @staticmethod
#     def create(food_item, category):
#         try:
#             FoodItemCategory.objects.create(food=food_item, category=category)
#         except IntegrityError:
#             raise AlreadyExists()
        
#     @staticmethod
#     def exists(id):
#         return FoodItemRelationChecker.exists(FoodItemCategory, id)


# class FoodItemCuisineRepository:
#     @staticmethod
#     def create(food_item, cuisine):
#         try:
#             FoodItemCuisine.objects.create(food=food_item, cuisine=cuisine)
#         except IntegrityError:
#             raise AlreadyExists()
        
#     @staticmethod
#     def exists(id):
#         return FoodItemRelationChecker.exists(FoodItemCuisine, id)


# class FoodItemCompositionRepository:
#     @staticmethod
#     def add(parent, child, amount):
#         FoodItemComposition.objects.create(parent=parent, child=child, amount=amount)