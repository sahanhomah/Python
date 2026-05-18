from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth import get_user_model
User = get_user_model()




# Create your views here.
def task(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html", {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        task_name = request.POST.get("task")
        if task_name:
            Task.objects.create(name=task_name)
        return redirect('listtasks')
    return render(request, "addtask.html")

def delete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    return redirect('listtasks')

def home(request):
    return render(request, "index.html")


