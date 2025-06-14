from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseForbidden
from django.views.decorators.http import require_GET, require_POST

from ..services import forms as service

@require_GET
def get_form(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    
    return service.get_form(request)


@require_POST
def submit_form(request):
    return service.submit_form(request)