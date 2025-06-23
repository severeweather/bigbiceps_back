from ..repositories.food_cuisine_repository import FoodCuisineRepository
from ..exeptions import IDNotFound, InvalidReference, AlreadyExists


class FoodCuisineService:

    @staticmethod
    def get_all():
        return FoodCuisineRepository.get_all()
    
    @staticmethod
    def get_by_id(id):
        try:
            return FoodCuisineRepository.get_by_id(id)
        except IDNotFound as e:
            raise InvalidReference(details=str(e))

    @staticmethod
    def get_form():
        return {
            "note": "Expecting list 'cuisines' of values type string."
        }
    
    @staticmethod
    def post_cuisines(cuisines):
        for cuisine in cuisines:
            try:
                FoodCuisineRepository.create(cuisine.capitalize())
            except AlreadyExists:
                continue