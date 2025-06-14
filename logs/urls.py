from django.urls import path

from .controllers import forms

urlpatterns = [
    path("form", forms.get_form, name="get_log_form"),
    path("form/submit", forms.submit_form, name="submit_log_form"),
]