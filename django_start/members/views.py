from urllib import request

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")  
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("gallery")
        else: 
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "authentication/login.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")

    return redirect("index")
