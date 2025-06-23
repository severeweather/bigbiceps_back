from ..repositories.food_item_cuisine_repository import FoodItemCuisineRepository
from ..exeptions import IDNotFound, InvalidReference, AlreadyExists
from .food_item_service import FoodItemService
from .food_cuisine_service import FoodCuisineService


class FoodItemCuisineService:

    @staticmethod
    def get_form():
        cuisines = FoodCuisineService.get_all()
        return {
            "note": "Expecting list 'cuisines' of cuisine id's",
            "cuisines": cuisines
        }

    @staticmethod
    def post_form(cuisines, id):
        food_item = FoodItemService.get_by_id(id)
    
        valid_cuisines = []

        for cuisine_id in cuisines:
            try:
                _ = FoodCuisineService.get_by_id(cuisine_id)
                valid_cuisines.append(_)
            except IDNotFound as e:
                raise InvalidReference(details=str(e))
        
        for valid_cuisine in valid_cuisines:
            try:
                FoodItemCuisineRepository.create(food_item, valid_cuisine)
            except AlreadyExists:
                continue

        return
    
    @staticmethod
    def exists(id):
        try:
            FoodItemCuisineRepository.exists(id)
        except IDNotFound as e:
            raise InvalidReference(details=str(e))