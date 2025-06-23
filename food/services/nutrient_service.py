from ..repositories.nutrient_repository import NutrientRepository
from ..exeptions import IDNotFound, InvalidReference, AlreadyExists


class NutrientService:

    @staticmethod
    def get_all():
        return NutrientRepository.get_all()
    
    @staticmethod
    def get_all_dict():
        return NutrientRepository.get_all_dict()
    
    @staticmethod
    def get_by_id(id):
        try:
            return NutrientRepository.get_by_id(id)
        except IDNotFound as e:
            raise InvalidReference(details=str(e))
   
    @staticmethod
    def get_form():
        return {
            "note": "Expecting list of key-value pairs with following structure. Structure: {name: unit}, where both 'name' and 'unit' are strings. Example: {'protein': 'g'}.",
        }

    @staticmethod
    def post_nutrients(nutrients):
        for key, value in nutrients.items():
            try:
                NutrientRepository.create(key.capitalize(), value)
            except AlreadyExists:
                continue