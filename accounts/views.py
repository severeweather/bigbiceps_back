from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt ## remove later

from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        next_url = request.GET.get('next', '/')

        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(next_url)
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    
    else:
        form = RegisterForm()
    return render(request, 'register.html', {"form": form})

@csrf_exempt
def log_in(request):
    if request.method == "POST":
        next_url = request.GET.get('next', '/')
        
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(next_url)
        else:
            return JsonResponse({"success": False, "errors": form.error_messages})
    
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

def log_out(request):
    logout(request)
    return redirect("homepage")