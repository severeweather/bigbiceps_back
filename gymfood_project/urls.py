from django.contrib import admin
from django.urls import path, include
from .views.pages import *

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("", homepage, name="homepage"),
    path("food/", include("food.urls")),
    path("logs/", include("logs.urls")),
    path("plate/", plate, name="plate"),
    path("auth/", include("accounts.urls")),

    path("api/logs/", include("logs.urls_api")),
    path("api/food/", include("food.urls_api")),
    path("api/social/", include("social.urls_api")),

    path("", include("social.urls")),
]