from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.http import JsonResponse, Http404, HttpResponseBadRequest, HttpResponseForbidden

from ..services import items as serve
from ..repository import items as repo


@require_GET
def get_item(request, id):
    """
    Controller. Checks whether id exists, returns instance or "False" accordingly.
    """
    item = repo.get_item(request, id)
    if not item:
        raise Http404()
    
    print('controller: success, returning item..')
    return JsonResponse({"success": True, "item": item}, status=200)

@require_GET
def get_bulk(request, logged):
    collection = repo.get_collection(request, logged=logged)
    

@login_required
def delete_item(request, id):
    """
    Controller. Either deletes instance by id or returns 404. Redirects to /food/ afterwards.
    """
    status = serve.delete_item(request, id)
    if status == 404:
        raise Http404()
    elif status == 403:
        return HttpResponseForbidden()
    
    print('controller: success, redirecting..')
    next_url = request.GET.get('next', '/home/')
    return redirect(next_url)

