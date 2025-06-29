from ..repositories.food_item_repository import FoodItemRepository as repo

class FoodItemSerializer:
    def __init__(self, obj):
        self.obj = obj

    def serialize(self, many: bool = True):
        self.obj = list(self.obj)
        if not many:
            return self.to_dict(self.obj[0])
        else:
            return [self.to_dict(o) for o in self.obj]
    
    def to_dict(self, obj):
        if obj.type == "dish":
            return {
                "id": obj.id,
                "name": obj.name,
                "type": obj.type,
                "description": obj.description,
                "recipe": obj.recipe,
            }
        else:
            return {
                "id": obj.id,
                "name": obj.name,
                "type": obj.type,
                "description": obj.description,
            }