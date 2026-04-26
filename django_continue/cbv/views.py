from django.shortcuts import render

# Create your views here.
def hello_world(request, name="World"):
    return render(request, "hello.html", {"name": name})