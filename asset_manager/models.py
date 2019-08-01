from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="users")
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()