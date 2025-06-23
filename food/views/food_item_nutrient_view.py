from django.views import View
from django.http import JsonResponse
from ..exeptions import internal_error, id_not_provided, response_ok, InvalidReference
from ..services.food_item_nutrient_service import FoodItemNutrientService as service
from .utils import validate_dict

class FoodItemNutrientView(View):
    def post(self, request, id=None):
        if id == None:
            return JsonResponse(id_not_provided(), status=400)
        
        if service.exists(id):
            return JsonResponse({"error:": "Nutrients are already added"}, status=400)
        
        try:
            nutrients = validate_dict(dict(request.POST), float)
            service.post_form(nutrients, id)
            return JsonResponse(response_ok(), status=201)

        except InvalidReference as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse(internal_error(e), status=500)