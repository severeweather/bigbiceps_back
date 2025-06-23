from ..forms import FoodItemForm
from ..repositories.food_item_repository import FoodItemRepository
from ..exeptions import IDNotFound, InvalidReference


class FoodItemService:
    @staticmethod
    def get_by_id(id):
        try:
            return FoodItemRepository.get_by_id(id)
        except IDNotFound as e:
            raise InvalidReference(details=str(e))
        
    @staticmethod
    def get_all_ingredients():
        return FoodItemRepository.get_all(food_type="ingredient")
    
    @staticmethod
    def get_all_dishes():
        return FoodItemRepository.get_all(food_type="dish")
    
    @staticmethod
    def get_all_meals():
        return FoodItemRepository.get_all(food_type="meal")

    @staticmethod
    def get_form(food_type):
        return {
            "form": FoodItemForm().Meta.fields,
            "type": food_type,
        }

    @staticmethod
    def create_food_item(request_user, food_type, **kwargs):
        form = FoodItemForm(kwargs)
        if form.is_valid():
            saved = form.save(commit=False)
            saved.type = food_type
            saved.created_by = request_user
            saved.save()
            return saved.id
        else:
            raise ValueError("Invalid form.")