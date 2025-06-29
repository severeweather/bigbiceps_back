from django.views import View
from django.http import JsonResponse
from ..services.food_item_service import FoodItemService as service
from ..exeptions import internal_error


class FoodItemView(View):
    food_type = None
    composition = []

    def get(self, request, id=None):
        if not id:
            return JsonResponse({"error": "Id parameter missing"}, status=400)
        pass
        
    def post(self, request, id=None):
        if id != None:
            return JsonResponse({"error": "POST request with id parameter not allowed"}, status=403)
        
        if self.food_type == None:
            return JsonResponse({"error": "Food type is not specified"}, status=500)
        
        try:
            food_item_id = service.create_food_item(
                request.user,
                food_type=self.food_type,
                name=request.POST.get("name", ""),
                description=request.POST.get("description", "")
            )
            return JsonResponse({"id": food_item_id, "food_type": self.food_type, "composition": self.composition}, status=201)

        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse(internal_error(e), status=500)

        
class IngredientView(FoodItemView):
    food_type = "ingredient"
    composition = []

class DishView(FoodItemView):
    food_type = "dish"
    composition = ["ingredient"]

class MealView(FoodItemView):
    food_type = "meal"
    composition = ["ingredient", "dish"]