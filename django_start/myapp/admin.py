from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "password")
    search_fields = ("username",)
    list_filter = ("username",)

admin.site.register(User, UserAdmin)
# Register your models here.
