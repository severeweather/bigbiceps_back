from food.services.food_item_service import FoodItemService as food_service
from food.serializers.food_item_serializer import FoodItemSerializer as food_serializer

## TEMPORARY COPY PASTE from foods/exceptions
class InvalidReference(Exception):
    def __init__(self, base_message="Invalid reference", code=0, details=None):
        self.base_message = base_message
        self.details = details
        self.code = code
        super().__init__(self.__str__())

    def __str__(self):
        if self.details:
            return f"{self.base_message}: {self.details}. code={self.code}"
        return f"{self.base_message}. code={self.code}"



VALID_FOOD_TYPES = ("ingredient", "dish", "meal")

class SearchFoodService:
    @staticmethod
    def validate_params(o, q, ft):
        try:
            for x in ft:
                if str(x) not in VALID_FOOD_TYPES:
                    raise ValueError(f"Invalid food type: {ft}")
            return int(o), str(q), ft
        except (ValueError, TypeError) as e:
            raise InvalidReference(details=str(e))

    @staticmethod
    def search(offset, query, food_type):
        try:
            offset, query, food_type = SearchFoodService.validate_params(offset, query, food_type)
        except (ValueError) as e:
            raise InvalidReference(details=str(e))
        
        limit = 10
        search_results = food_service.filter(food_type=food_type, name=query).order_by("name")
        batch = search_results[offset:offset + limit + 1]

        serialized_batch = food_serializer(batch).serialize(many=True)

        has_next = len(serialized_batch) > limit

        return list(serialized_batch[:limit]), has_next