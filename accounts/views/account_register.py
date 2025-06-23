from django.views import View
from ..services.custom_user import CustomUserService
from ..exceptions import MissingCredentials, InvalidCredentials
from django.http import JsonResponse
from django.contrib.auth import login


class AccountRegisterView(View):
    def get(self, request):
        pass

    def post(self, request):
        try:
            user = CustomUserService.create(
                username=request.POST.get("username", ""),
                email=request.POST.get("email", ""),
                password1=request.POST.get("password1", ""),
                password2=request.POST.get("password2", ""),
            )
            login(request, user)
            return JsonResponse({}, status=201)
        
        except InvalidCredentials as e:
            return JsonResponse({"error": e.error}, status=400)
        
        except MissingCredentials as e:
            return JsonResponse({"error": e.error}, status=400)
        
        except Exception as e:
            return JsonResponse({"error": f"Internal server error: {str(e)}"})