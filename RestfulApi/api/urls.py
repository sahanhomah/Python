from django.urls import include, path
from . import views
urlpatterns = [
    path('students/', views.studentViews),
    path('students/<int:pk>/', views.studentDetailViews),
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeesDetail.as_view()),
]   