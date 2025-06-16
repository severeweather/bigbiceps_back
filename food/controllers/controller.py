from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from django.middleware.csrf import get_token
import json

from ..services.service import *
from ..exceptions.exeptions import MissingField, InvalidReference


class ControllerTools:

    @staticmethod
    def validate_dict(d, value_type):
        for key, value in d.items():
            if isinstance(value, list):
                value = value[0]
            try:
                d[key] = value_type(value)
            except (TypeError, ValueError) as e:
                raise InvalidReference(f"Invalid reference {str(e)}")
        return d

    @staticmethod
    def food_type_is_valid(id, *args):
        food_item = FoodItemService.get_by_id(id)
        if not food_item.type in args:
            return False
        
        return True
    
    
class NutrientController:
    @staticmethod
    def get_form(request):
        return JsonResponse({"data": NutrientService.get_form(), "csrf_token": get_token(request)})
    
    @staticmethod
    def post_form(request):
        nutrients = ControllerTools.validate_dict(dict(request.POST), str)
        NutrientService.post_form(nutrients)
        return JsonResponse({})


class FoodCategoryController:
    @staticmethod
    def get_form(request):
        return JsonResponse({"data": FoodCategoryService.get_form(), "csrf_token": get_token(request)})
    
    @staticmethod
    def post_form(request):
        categories = request.POST.getlist("categories", "")
        FoodCategoryService.post_form(categories)
        return JsonResponse({})

               
class FoodCuisineController:
    @staticmethod
    def get_form(request):
        return JsonResponse({"data": FoodCuisineService.get_form(), "csrf_token": get_token(request)})
    
    @staticmethod
    def post_form(request):
        cuisines = request.POST.getlist("cuisines", "")
        FoodCuisineService.post_form(cuisines)
        return JsonResponse({})
    

class FoodItemController:

    @staticmethod
    def get_form(request, food_type):
        return JsonResponse({"data": FoodItemService.get_form(food_type), "csrf_token": get_token(request)}, status=200)
    
    @staticmethod
    def post_form(request, food_type):
        try:
            id = FoodItemService.post_form(request.user, food_type, request.POST)
            if food_type == "ingredient":
                return JsonResponse({"redirect_to": f"/food/{id}/nutrients"})
            else:
                return JsonResponse({"redirect_to": f"/food/{id}/composition"})
            
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)


class FoodItemNutrientController:

    @staticmethod
    def get_form(request, id):
        return JsonResponse({"data": FoodItemNutrientService.get_form(), "id": id, "csrf_token": get_token(request)})

    @staticmethod
    def post_form(request, id):
        try:
            if FoodItemNutrientService.exists(id):
                return JsonResponse({"error": "Nutrients already exist.", "redirect_to": f"/food/{id}/categories"})
            
            nutrients = ControllerTools.validate_dict(dict(request.POST))
            FoodItemNutrientService.post_form(nutrients, id)
            return JsonResponse({"redirect_to": f"/food/{id}/categories"})
        
        except (MissingField, InvalidReference) as e:
            return JsonResponse({"error": str(e)}, status=400)

    
class FoodItemCategoryController:

    @staticmethod
    def get_form(request, id):
        return JsonResponse({"data": FoodItemCategoryService.get_form(), "id": id, "csrf_token": get_token(request)})

    @staticmethod
    def post_form(request, id):
        try:
            if FoodItemCategoryService.exists(id):
                return JsonResponse({"message": "Categories already exist.", "redirect_to": f"/food/{id}/cuisines"})
            
            categories = request.POST.getlist("categories")
            FoodItemCategoryService.post_form(categories, id)
            return JsonResponse({"redirect_to": f"/food/{id}"})

        except InvalidReference as e:
            return JsonResponse({"ok": False, "error": str(e)}, status=400)


class FoodItemCuisineController:

    @staticmethod
    def get_form(request, id):
        return JsonResponse({"data": FoodItemCuisineService.get_form(), "id": id, "csrf_token": get_token(request)})
    
    @staticmethod
    def post_form(request, id):
        try:
            if FoodItemCuisineService.exists(id):
                return JsonResponse({"message": "Cuisines already exist.", "redirect_to": f"/food/{id}/composition"})
            
            cuisines = request.POST.getlist("cuisines")
            FoodItemCuisineService.post_form(cuisines, id)
            return JsonResponse({"redirect_to": f"/food/{id}"})

        except InvalidReference as e:
            return JsonResponse({"ok": False, "error": str(e)}, status=400)


class FoodItemChildController:

    @staticmethod
    def get_form(request, id):
        return JsonResponse({"data": FoodItemChildService.get_form(id), "id": id, "csrf_token": get_token(request)})
    
    @staticmethod
    def post_form(request, id):
        try:
            food_item = FoodItemService.get_by_id(id)

            children_list = ControllerTools.validate_dict(dict(request.POST))
            FoodItemChildService.post_form(id, children_list)
            if food_item.type == "dish":
                return JsonResponse({"redirect_to": f"/food/{id}/cuisines"})
            else:
                return JsonResponse({"redirect_to": f"/food/{id}"})

        except InvalidReference as e:
            return JsonResponse({"error": str(e)}, status=400)



def page(request):
    return render(request, 'page.html', {})


def details(request, id):
    pass


@login_required
def form(request, food_type):
    if not food_type in ["ingredient", "dish", "meal"]:
        return JsonResponse({"error": f"Invalid food type {food_type}"}, status=400)
    
    if request.method == "GET":
        return FoodItemController.get_form(request, food_type)
        
    elif request.method == "POST":
        return FoodItemController.post_form(request, food_type)
        
    else:
        return HttpResponseNotAllowed(["GET", "POST"])
    

@login_required
def nutrients(request, id=None):
    if not id:
        return JsonResponse({"error": "No id provided"}, status=400)

    if not ControllerTools.food_type_is_valid(id, "ingredient"):
        return JsonResponse({"error": "Invalid food type"}, status=400)

    if request.method == "GET":
        return FoodItemNutrientController.get_form(request, id)

    elif request.method == "POST":
        return FoodItemNutrientController.post_form(request, id)
        
    else:
        return HttpResponseNotAllowed(["GET", "POST"])
    

@login_required
def categories(request, id=None):
    if not id:
        return JsonResponse({"error": "No id provided"}, status=400)

    if not ControllerTools.food_type_is_valid(id, "ingredient"):
        return JsonResponse({"error": "Invalid food type"}, status=400)
    
    if request.method == "GET":
        return FoodItemCategoryController.get_form(request, id)
    
    elif request.method == "POST":
        return FoodItemCategoryController.post_form(request, id)
        
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@login_required
def cuisines(request, id=None):
    if not id:
        return JsonResponse({"error": "No id provided"}, status=400)

    if not ControllerTools.food_type_is_valid(id, "dish"):
        return JsonResponse({"error": "Invalid food type"}, status=400)
    
    if request.method == "GET":
        return FoodItemCuisineController.get_form(request, id)
    
    elif request.method == "POST":
        return FoodItemCuisineController.post_form(request, id)
        
    else:
        return HttpResponseNotAllowed(["GET", "POST"])
    

@login_required
def composition(request, id=None):
    if not id:
        return JsonResponse({"error": "No id provided"}, status=400)

    if not ControllerTools.food_type_is_valid(id, "dish", "meal"):
        return JsonResponse({"error": "Invalid food type"}, status=400)
    
    if request.method == "GET":
        return FoodItemChildController.get_form(request, id)
    
    elif request.method == "POST":  
        return FoodItemChildController.post_form(request, id)

    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@login_required
def nutrients(request):

    if request.method == "GET":
        return NutrientController.get_form(request)
    
    elif request.method == "POST":
        return NutrientController.post_form(request)

    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@login_required
def categories(request):

    if request.method == "GET":
        return FoodCategoryController.get_form(request)
    elif request.method == "POST":
        return FoodCategoryController.post_form(request)
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@login_required
def cuisines(request):

    if request.method == "GET":
        return FoodCuisineController.get_form(request)
    elif request.method == "POST":
        return FoodCuisineController.post_form(request)
    else:
        return HttpResponseNotAllowed(["GET", "POST"])

