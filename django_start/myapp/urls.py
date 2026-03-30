from django.urls import path
from . import views
urlpatterns=[
    path("", views.index, name="index"),
    path("gallery/", views.gallery, name="gallery"),
    path("about/", views.about, name="about"),
    path("stats/", views.blog, name="stats"),
    path("blog/", views.blog, name="blog"),
    path("tasks/", views.task_list, name="task_list"),
    path("tasks/new/", views.task_create, name="task_create"),
    path("tasks/<int:task_id>/edit/", views.task_update, name="task_update"),
    path("tasks/<int:task_id>/delete/", views.task_delete, name="task_delete"),
    path("userform/", views.userform, name="userform"),
    path("output/", views.output, name="output"),
    path("users-table/", views.users_table, name="users_table"),
    path("users-table/<int:user_id>/edit/", views.edit_user, name="edit_user"),
    path("users-table/<int:user_id>/delete/", views.delete_user, name="delete_user"),
 ]