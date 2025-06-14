from django.urls import path

from logs.api_controllers.logs_instance_handler import logs_instance_handler
from logs.api_controllers.logs_all import logs_all

urlpatterns = [
    path("", logs_all, name="api_logs_all"),
    path("<uuid:id>", logs_instance_handler, name="api_logs_instance_handler"),
]