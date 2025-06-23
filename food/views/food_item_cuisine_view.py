from django.views import View
from django.http import JsonResponse
from ..exeptions import internal_error, response_ok, InvalidReference
from ..services.food_item_cuisine_service import FoodItemCuisineService as service

class FoodItemCuisineView(View):
    def post(self, request, id=None):
        try:
            if service.exists(id):
                return JsonResponse({"error": "Cuisines are already added"}, status=400)
            
            cuisines = request.POST.getlist("cuisines", "")
            service.post_form(cuisines, id)
            return JsonResponse(response_ok(), status=201)

        except InvalidReference as e:
            return JsonResponse({"error": str(e)}, 400)
        except Exception as e:
            return JsonResponse(internal_error(e), status=500)