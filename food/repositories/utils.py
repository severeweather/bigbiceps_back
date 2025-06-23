from ..models import FoodItem
from ..exeptions import IDNotFound


class FoodItemRelationChecker:
    @staticmethod
    def exists(model, food_item_id):
        try:
            food_item = FoodItem.objects.get(id=food_item_id)
            return model.objects.filter(food=food_item).exists()
        except FoodItem.DoesNotExist:
            raise IDNotFound(FoodItem, food_item_id)