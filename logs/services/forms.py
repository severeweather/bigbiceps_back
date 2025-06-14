from django.shortcuts import render
from django.http import JsonResponse

from ..forms import MealLogForm


def get_form(request):
    new_form = MealLogForm()
    return render(request, f"logs/form/form.html", {
        "form": new_form,
    })

def submit_form(request):
    new_form = MealLogForm(request.POST)
    if new_form.is_valid():
        nf = new_form.save(commit=False)
        nf.user = request.user
        nf.save()
        return JsonResponse({"success": True}, status=200)
    else:
        return JsonResponse({"success": False, "errors": new_form.errors}, status=400)