from django.urls import path

from .controllers.controller import *

urlpatterns = [
    path("", page, name="food"),


    path("new/<str:food_type>", form, name="food__form"),

    path("<uuid:id>", details, name="food__details"),

    path("<uuid:id>/nutrients", nutrients, name="food__nutrients"),
    path("<uuid:id>/categories", categories, name="food__categories"),
    path("<uuid:id>/cuisines", cuisines, name="food__cuisines"),
    path("<uuid:id>/composition", composition, name="food__composition"),
    

    # #TODO
    # path("admin/form/nutrient", form_nutrient, name="form_nutrient"),   
    # path("admin/form/category", form_category, name="form_category"),   
    # path("admin/form/cuisine", form_cuisine, name="form_cuisine"),   
]