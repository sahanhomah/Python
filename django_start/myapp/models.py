from django.db import models

# Create your models here.
class User(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(unique=True)
    password= models.CharField(max_length=100)
    address= models.CharField(max_length=200, default="unknown")
    contact= models.CharField(max_length=15, default="unknown")
    def __str__(self):
        return self.name


class Task(models.Model):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

    STATUS_CHOICES = [
        (TODO, "To Do"),
        (IN_PROGRESS, "In Progress"),
        (DONE, "Done"),
    ]

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    PRIORITY_CHOICES = [
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    ]

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    work_update = models.TextField(blank=True, default="")
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TODO)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=MEDIUM)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
