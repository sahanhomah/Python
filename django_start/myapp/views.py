from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import localdate

from myapp.models import Task
  
from .forms import TaskForm, TaskUpdateForm

# Create your views here.
def index(request):
    return render(request, 'home.html')
def gallery(request):
    context = {
        "name": "Sahan",
    }
    return render(request, 'about.html', context)


def about(request):
    return gallery(request)


def blog(request):
    context = {
        "name": "Neymar Jr",
        "stats": [
            {"label": "International Caps", "value": "128+"},
            {"label": "International Goals", "value": "79+"},
            {"label": "Career Club Goals", "value": "400+"},
            {"label": "Career Assists", "value": "250+"},
        ],
        "achievements": [
            "UEFA Champions League winner (Barcelona)",
            "Olympic Gold Medal with Brazil (2016)",
            "Copa Libertadores winner with Santos",
            "Multiple Ligue 1 titles with PSG",
            "One of Brazil's all-time top scorers",
        ],
    }
    return render(request, 'blog.html', context)


def userform(request):
    return task_create(request)




def output(request):
    return redirect("task_list")


def users_table(request):
    return task_list(request)


def task_list(request):
    status_filter = request.GET.get("status", "all")
    tasks = Task.objects.all().order_by("due_date", "-created_at")

    if status_filter in {Task.TODO, Task.IN_PROGRESS, Task.DONE}:
        tasks = tasks.filter(status=status_filter)

    context = {
        "tasks": tasks,
        "today": localdate(),
        "status_filter": status_filter,
        "status_options": [
            ("all", "All"),
            (Task.TODO, "To Do"),
            (Task.IN_PROGRESS, "In Progress"),
            (Task.DONE, "Done"),
        ],
    }
    return render(request, "users_table.html", context)


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("task_update", task_id=task.id)
    else:
        form = TaskForm()

    return render(request, "userform.html", {"form": form, "page_title": "Create Task", "submit_label": "Create Task"})


def edit_user(request, user_id):
    return task_update(request, user_id)


def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskUpdateForm(instance=task)

    return render(request, "user_edit.html", {"form": form, "task": task})


def delete_user(request, user_id):
    return task_delete(request, user_id)


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
    return redirect("task_list")


def task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.status = Task.DONE
        task.save(update_fields=["status", "updated_at"])
    return redirect("task_list")

def admin(request):
    return redirect("/admin/")