from django.urls import include, path
from . import views
urlpatterns = [
    path('students/', views.studentViews),
    path('students/<int:pk>/', views.studentDetailViews),
]