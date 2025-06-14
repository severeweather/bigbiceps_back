from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from logs.models import MealLog

def get_item(request, id):
    """
    Repository. Looks for matching id in logs. 
    Returns instance or "False" accordingly.
    """
    item = MealLog.objects.filter(id=id).first()
    if item:
        print(f"repo: item found: {item}")
        return item
        
    print(f'repo: item id "{id}" not found')
    return False

def get_collection(request, **kwargs):
    """
    Repository. Retrieves a collection of MealLog instances based on filters.
    """
    allowed_filters = {"id", "user", "logged"}
    filters = {k: v for k, v in kwargs.items() if k in allowed_filters}

    collection = MealLog.objects.filter(user=request.user, **filters).order_by("-logged")
    return collection


def delete_item(request, id):
    """
    Repository. Either deletes an instance or does nothing.
    """
    item = get_item(request, id)
    if not item:
        print(f'repo: item id "{id}" was not deleted, not found')
        return
    
    item.delete()
    print(f'repo: item id "{id}" was deleted')
    return
