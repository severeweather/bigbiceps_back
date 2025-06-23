from ..repositories.food_item_nutrient_repository import FoodItemNutrientRepository
from ..exeptions import IDNotFound, InvalidReference, AlreadyExists
from .nutrient_service import NutrientService
from .food_item_service import FoodItemService

class FoodItemNutrientService:

    @staticmethod
    def validate_amount(amount):
        try:
            amount = float(amount)
        except ValueError:
            return 0

        if amount < 0 or amount > 10000:
            raise ValueError("Amount must be an integer within interval [0-10000]")
        return amount

    @staticmethod
    def get_food_item_nutrients(id):
        try:
            return FoodItemNutrientRepository.get_food_item_nutrients(id)
        except IDNotFound as e:
            raise InvalidReference(details=str(e))

    @staticmethod
    def get_form():
        nutrients = NutrientService.get_all()
        return {
            "note": "Expecting list of key-value pairs, where key is nutrient's id and value is amount in nutrient's units",
            "nutrients": nutrients
        }

    @staticmethod
    def post_form(nutrients, id):
        food_item = FoodItemService.get_by_id(id)
        
        valid_nutrients = NutrientService.get_all_dict()

        for n in nutrients.keys():
            if n not in valid_nutrients.keys():
                raise InvalidReference()

            try:
                nutrient = NutrientService.get_by_id(n)
                amount = FoodItemNutrientService.validate_amount(nutrients[n])
            except (IDNotFound, ValueError) as e:
                raise InvalidReference(details=str(e))

            try:
                FoodItemNutrientRepository.create(food_item, nutrient, amount)
            except AlreadyExists as e:
                raise InvalidReference(details=str(e))
            
    @staticmethod
    def exists(id):
        try:
            return FoodItemNutrientRepository.exists(id)
        except IDNotFound as e:
            raise InvalidReference(details=str(e))