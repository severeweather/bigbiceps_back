from django.http import JsonResponse
from django.views import View
from ..services.nutrient_service import NutrientService as service
from .utils import validate_dict
from ..exeptions import InvalidReference, AlreadyExists, internal_error, response_ok


class NutrientView(View):
    def get(self, request):
        return JsonResponse({"nutrients": service.get_all()}, status=200)

    def post(self, request):
        try:
            nutrients = validate_dict(dict(request.POST), str)
            service.post_nutrients(nutrients)
            return JsonResponse(response_ok(), status=201)
        
        except (InvalidReference, AlreadyExists) as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse(internal_error(e), status=500)