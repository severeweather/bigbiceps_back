from ..repositories.food_category_repository import FoodCategoryRepository
from ..exeptions import IDNotFound, InvalidReference, AlreadyExists


class FoodCategoryService:

    @staticmethod
    def get_all():
        return FoodCategoryRepository.get_all()
    
    @staticmethod
    def get_by_id(id):
        try:
            return FoodCategoryRepository.get_by_id(id)
        except IDNotFound as e:
            raise InvalidReference(details=str(e))
    
    @staticmethod
    def get_form():
        return {
            "note": "Expecting list 'categories' of values type string."
        }
    
    @staticmethod
    def post_categories(categories):
        for category in categories:
            try:
                FoodCategoryRepository.create(category.capitalize())
            except AlreadyExists:
                continue