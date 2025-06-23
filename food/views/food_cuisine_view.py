from django.views import View
from django.http import JsonResponse
from ..exeptions import response_ok, internal_error
from ..services.food_cuisine_service import FoodCuisineService as service


class FoodCuisineView(View):
    def get(self, request):
        return JsonResponse({"cuisines": service.get_all()}, status=200)
    
    def post(self, request):
        try:
            cuisines = request.POST.getlist("cuisines", "")
            service.post_cuisines(cuisines)
            return JsonResponse(response_ok(), status=201)
        except Exception as e:
            return JsonResponse(internal_error(e), status=500)