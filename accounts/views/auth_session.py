from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

@method_decorator(ensure_csrf_cookie, name='get')
class AuthSession(View):
    def get(self, request):
        return JsonResponse({
            "is_authenticated": request.user.is_authenticated,
            "user": {
                "id": request.user.id,
                "username": request.user.username,
            } if request.user else None
        })