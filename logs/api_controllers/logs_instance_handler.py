from django.http import HttpResponseNotAllowed

from logs.controllers import items as controller

def logs_instance_handler(request, id):
    if request.method == "GET":
        return controller.get_item(request, id)
    elif request.method == "DELETE":
        return controller.delete_item(request, id)
    
    return HttpResponseNotAllowed(["GET", "DELETE"])