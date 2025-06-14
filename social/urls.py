from django.urls import path

from .views import profile, profile_manager

urlpatterns = [
    path("<str:username>/", profile, name="profile"),
    path("profile/edit/", profile_manager, name="profile_manager"),
]