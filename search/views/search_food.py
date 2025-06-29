from django.views import View
from django.http import JsonResponse
from ..services.search_food_service import SearchFoodService as service

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

class SearchFoodView(View):
    def get(self, request):
        offset = request.GET.get("o", 0)
        query = request.GET.get("q", "")
        food_type = request.GET.getlist("ft", "")

        try:
            search_results, has_next = service.search(offset, query, food_type)
            return JsonResponse({"search_results": search_results, "has_next": has_next}, status=200)
        except InvalidReference as e:
            return JsonResponse({"error": str(e)}, status=400)
