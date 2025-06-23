from django.urls import path
from .views.nutrient_view import NutrientView
from .views.food_category_view import FoodCategoryView
from .views.food_cuisine_view import FoodCuisineView
from .views.food_item_view import IngredientView, DishView, MealView
from .views.food_item_nutrient_view import FoodItemNutrientView
from .views.food_item_category_view import FoodItemCategoryView
from .views.food_item_cuisine_view import FoodItemCuisineView
from .views.food_item_composition_view import FoodItemCompositionView


urlpatterns = [
    path("nutrient", NutrientView.as_view(), name="food__nutrient"),
    path("category", FoodCategoryView.as_view(), name="food__category"),
    path("cuisine", FoodCuisineView.as_view(), name="food__cuisine"),

    path("ingredient", IngredientView.as_view(), name="food__ingredient"),
    path("dish", DishView.as_view(), name="food__dish"),
    path("meal", MealView.as_view(), name="food__meal"),

    path("<uuid:id>/nutrients", FoodItemNutrientView.as_view(), name="food__food_item_nutrients"),
    path("<uuid:id>/categories", FoodItemCategoryView.as_view(), name="food__food_item_categories"),
    path("<uuid:id>/cuisines", FoodItemCuisineView.as_view(), name="food__food_item_cuisines"),
    path("<uuid:id>/composition", FoodItemCompositionView.as_view(), name="food__food_item_composition"),
]