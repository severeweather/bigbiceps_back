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
    def food_type_is_valid(id, *args):
        food_item = FoodItemService.get_by_id(id)
        if not food_item.type in args:
            return False
        
        return True


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
            
            nutrients = dict(request.POST)
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

            data = json.loads(request.body)
            children_list = data["children_list"]
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
        return HttpResponseNotAllowed(["POST", "GET"])










# # ADMIN TODO
# @login_required
# def form_nutrient(request):
#     VALID_ACTIONS = {
#             "save_go_home": 'homepage',
#             "save_one_more": 'form_nutrient'
#         }
#     if request.method == "POST":
#         action = request.POST.get("action")
#         if action not in VALID_ACTIONS.keys():
#             return JsonResponse({"ok": False, "error": "Invalid save action"}, status=403)

#         name = request.POST.get("name", "")
#         unit = request.POST.get("unit", "")

#         try:
#             service.post_form_nutrient(name=name, unit=unit)
#             return redirect(VALID_ACTIONS[action])
#         except (InvalidReference, ValueError) as e:
#             return JsonResponse({"ok": False, "error": str(e)}, status=400)

#     elif request.method == "GET":
#         return render(request, "form_nutrient.html", service.get_form_nutrient_data())
    
#     else:
#         return HttpResponseNotAllowed(["POST", "GET"])
    
# @login_required
# def form_category(request):
#     VALID_ACTIONS = {
#             "save_go_home": 'homepage',
#             "save_one_more": 'form_category'
#         }
#     if request.method == "POST":
#         action = request.POST.get("action")
#         if action not in VALID_ACTIONS.keys():
#             return JsonResponse({"ok": False, "error": "Invalid save action"}, status=403)
        
#         name = request.POST.get("name")

#         if not name:
#             return JsonResponse({"ok": False, "error": "'name' value is missing"}, status=403)

#         try:
#             service.post_form_category(name)
#             return redirect(VALID_ACTIONS[action])
#         except (InvalidReference, ValueError) as e:
#             return JsonResponse({"ok": False, "error": str(e)}, status=400)
            
#     elif request.method == "GET":
#         return render(request, "form_category.html", service.get_form_category_data())
#     else:
#         return HttpResponseNotAllowed(["POST", "GET"])
    
# @login_required
# def form_cuisine(request):
#     VALID_ACTIONS = {
#             "save_go_home": 'homepage',
#             "save_one_more": 'form_cuisine'
#         }
#     if request.method == "POST":
#         action = request.POST.get("action")
#         if action not in VALID_ACTIONS.keys():
#             return JsonResponse({"ok": False, "error": "Invalid save action"}, status=403)
        
#         name = request.POST.get("name")

#         if not name:
#             return JsonResponse({"ok": False, "error": "'name' value is missing"}, status=403)

#         try:
#             service.post_form_cuisine(name)
#             return redirect(VALID_ACTIONS[action])
#         except (InvalidReference, ValueError) as e:
#             return JsonResponse({"ok": False, "error": str(e)}, status=400)
            
#     elif request.method == "GET":
#         return render(request, "form_cuisine.html", service.get_form_cuisine_data())
#     else:
#         return HttpResponseNotAllowed(["POST", "GET"])

