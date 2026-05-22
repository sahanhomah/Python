from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
# Create your views here.
def studentViews(request):
    students = Student.objects.all()
    students = list(students.values())
    return JsonResponse(students, safe=False)