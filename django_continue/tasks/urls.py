from django.urls import path
from . import views

urlpatterns = [
    path('', views.task, name='listtasks'),
    path('add/', views.add_task, name='addtask'),
    path('delete/<int:task_id>/', views.delete_task, name='deletetask'),
    path('home/', views.home, name='home'),
    
]
