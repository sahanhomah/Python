from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')


urlpatterns = [
    path('students/', views.studentViews),
    path('students/<int:pk>/', views.studentDetailViews),
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeesDetail.as_view()),
    path('', include(router.urls)),
    path ('blogs/', views.BlogView.as_view(), name='blog-view'),
    path('comments/', views.CommentView.as_view(), name='comment-view'),
]   