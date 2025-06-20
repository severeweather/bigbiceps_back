from django.views import View
from django.contrib.auth import logout
from django.http import JsonResponse


class AccountLogoutView(View):
    def get(self, request):
        pass

    def post(self, request):
        logout(request)
        return JsonResponse({}, status=200)