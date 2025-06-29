from django.views import View
from django.http import JsonResponse
from ..exeptions import internal_error, id_not_provided, response_ok, InvalidReference
from ..services.food_item_composition_service import FoodItemCompositionService as service
from .utils import validate_dict


class FoodItemCompositionView(View):
    def post(self, request, id=None):
        try:
            if id == None:
                return JsonResponse(id_not_provided(), status=400)

            children_list = validate_dict(dict(request.POST), float)
            print(children_list)
            service.post_form(id, children_list)
            return JsonResponse(response_ok(), status=201)
            
        except InvalidReference as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse(internal_error(e), status=500)