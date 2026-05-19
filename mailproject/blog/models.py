from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.
class CustomUser(AbstractUser):
    username=None
    phone_number = models.CharField(max_length=10, unique=True  )
    user_bio = models.TextField(blank=True, null=True)
    user_image = models.ImageField(upload_to='profile', blank=True, null=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()