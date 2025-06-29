from django.urls import path
from .views.search_food import SearchFoodView

urlpatterns = [
    path("food", SearchFoodView.as_view(), name="search__food_search"),
]