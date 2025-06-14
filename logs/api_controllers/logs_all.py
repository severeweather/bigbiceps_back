from django.http import HttpResponseNotAllowed, JsonResponse
from datetime import datetime

from logs.repository import items as repo

def logs_all(request):
    if request.method == "GET":
        today = datetime.now().strftime("%Y-%m-%d")
        logged = request.GET.get("logged", today)
        try:
            datetime.strptime(logged, "%Y-%m-%d")
        except ValueError:
            return JsonResponse({"success": False, "error": "Invalid date format. Use YYYY-MM-DD."}, status=400)
        
        collection = repo.get_collection(request, logged=logged)
        return JsonResponse({"success": True, "collection": list(collection.values())}, status=200)

    return HttpResponseNotAllowed(["GET"])