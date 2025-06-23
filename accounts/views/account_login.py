from django.http import JsonResponse
from django.views import View
from django.contrib.auth import login
from ..services.custom_user import CustomUserService
from ..exceptions import MissingCredentials, InvalidCredentials


class AccountLoginView(View):

    def get(self, request):
        pass

    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        
        try:
            user = CustomUserService.login(username, password)
            login(request, user)
            return JsonResponse({"message": "Login successful"}, status=200)
        except (MissingCredentials, InvalidCredentials) as e:
            return JsonResponse({"error": str(e)}, status=400)