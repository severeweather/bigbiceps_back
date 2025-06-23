from ..models import FoodItem
from ..exeptions import IDNotFound


class FoodItemRepository:
    @staticmethod
    def get_by_id(id):
        try:
            return FoodItem.objects.get(id=id)
        except FoodItem.DoesNotExist:
            raise IDNotFound(FoodItem, id)
        
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