from ..repositories.food_item_composition_repository import FoodItemCompositionRepository
from ..exeptions import IDNotFound, InvalidReference
from .food_item_service import FoodItemService
from .food_item_nutrient_service import FoodItemNutrientService


class FoodItemCompositionService:

    @staticmethod
    def validate_amount(amount):
        amount = int(amount)
        if amount < 0 or amount > 100:
            raise ValueError("Amount must be an integer within interval [1-100]")
        return amount
    
    
    @staticmethod
    def get_form(id):
        food_item = FoodItemService.get_by_id(id)
        if food_item.type == "dish":
            food_type = ["ingredient"]
        elif food_item.type == "meal":
            food_type = ["ingredient", "dish"]
            
        return {
            "note": "Expecting a dict with following structure",
            "note 2": "amount type 'float' min 0.1 max 100",
            "structure": [
                {
                    "uuid": "amount"
                }
            ]
        }
        

    @staticmethod
    def post_form(parent_id, children_list):
        parent = FoodItemService.get_by_id(parent_id) 

        good_children = {}

        for id, amount in children_list.items():
            try:
                good_child = FoodItemService.get_by_id(id)
                amount = FoodItemCompositionService.validate_amount(amount)
                good_children[id] = amount

            except (IDNotFound, KeyError, ValueError) as e:
                raise InvalidReference(details=str(e))
        
        parent_nutrients = {}

        for id1, amount1 in good_children.items():
            child_nutrients = FoodItemNutrientService.get_food_item_nutrients(id1)

            for id2, amount2 in child_nutrients.items():
                amount = round(float(amount2) * float(amount1), 2)

                if id2 in parent_nutrients:
                    parent_nutrients[str(id2)] += amount
                else:
                    parent_nutrients[str(id2)] = amount

        FoodItemNutrientService.post_form(parent_nutrients, parent_id)

        for id, amount in good_children.items():
            good_child = FoodItemService.get_by_id(id)
            FoodItemCompositionRepository.add(parent, good_child, amount)