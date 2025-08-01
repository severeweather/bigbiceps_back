from django.urls import path

from .controllers.controller import *

from .models import FoodItem

def delete_all(request):
    FoodItem.objects.all().delete()
    return JsonResponse({})

urlpatterns = [
    path("", page, name="food"),

    path("new/nutrients", nutrients, name="food__nutrients"),
    path("new/categories", categories, name="food__categories"),
    path("new/cuisines", cuisines, name="food__cuisines"),

    path("new/<str:food_type>", form, name="food__form"),

    path("<uuid:id>", details, name="food__details"),

    path("<uuid:id>/nutrients", nutrients, name="food__nutrients"),
    path("<uuid:id>/categories", categories, name="food__categories"),
    path("<uuid:id>/cuisines", cuisines, name="food__cuisines"),
    path("<uuid:id>/composition", composition, name="food__composition"),
    

    # path("delete/all", delete_all, name="name")
]