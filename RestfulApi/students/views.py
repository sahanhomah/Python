from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def Students(request):
    Student=[{"name": "Sahan", "age": 22, "grade": "A"},]
    return HttpResponse(Student)