from django.views import View
from django.http import JsonResponse
from ..services.food_category_service import FoodCategoryService as service
from ..exeptions import internal_error, response_ok


class FoodCategoryView(View):
    def get(self, request):
        return JsonResponse({"categories": service.get_all()}, status=200)

    def post(self, request):
        try:
            categories = request.POST.getlist("categories", "")
            service.post_categories(categories)
            return JsonResponse(response_ok(), status=201)
        except Exception as e:
            return JsonResponse(internal_error(e), status=500)