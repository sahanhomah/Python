from django.urls import path
from . import views

urlpatterns = [
    path('isitsunday', views.sunday, name='checkingsunday'),
    
]