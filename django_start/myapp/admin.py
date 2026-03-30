from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name')
    list_filter = ('name',)

admin.site.register(User)
# Register your models here.
