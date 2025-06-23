from ..repositories.food_item_category_repository import FoodItemCategoryRepository
from ..exeptions import IDNotFound, InvalidReference, AlreadyExists
from .food_category_service import FoodCategoryService
from .food_item_service import FoodItemService


class FoodItemCategoryService:

    @staticmethod
    def get_form():
        categories = FoodCategoryService.get_all()
        return {
            "note": "Expecting list 'categories' of category id's",
            "categories": categories
            }

    @staticmethod
    def post_form(categories, id):
        food_item = FoodItemService.get_by_id(id)

        valid_categories = []

        for category_id in categories:
            try:
                _ = FoodCategoryService.get_by_id(category_id)
                valid_categories.append(_)
            except IDNotFound as e:
                raise InvalidReference(details=str(e))
        
        for valid_category in valid_categories:
            try:
                FoodItemCategoryRepository.create(food_item, valid_category)
            except AlreadyExists:
                continue

        return
    
    @staticmethod
    def exists(id):
        try:
            FoodItemCategoryRepository.exists(id)
        except IDNotFound as e:
            raise InvalidReference(details=str(e))