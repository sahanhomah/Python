from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User.objects.create_user(username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(update_fields=["is_staff", "is_superuser"])
        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "authentication/signup.html")


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
