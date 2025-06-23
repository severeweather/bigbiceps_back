from ..models import FoodItemComposition


class FoodItemCompositionRepository:
    @staticmethod
    def add(parent, child, amount):
        FoodItemComposition.objects.create(parent=parent, child=child, amount=amount)