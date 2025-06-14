from django.urls import path

from .views import follow_or_unfollow

urlpatterns = [
    path("follow-unfollow/<uuid:id>", follow_or_unfollow, name="follow_or_unfollow"),
]