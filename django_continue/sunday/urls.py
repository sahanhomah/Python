from django.urls import path
from . import views

urlpatterns = [
    path('', views.sunday, name='checkingsunday'),
    
]