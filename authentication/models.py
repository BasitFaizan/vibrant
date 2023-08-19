from django.contrib.auth.models import AbstractUser
from django.db import models

class customUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=15, blank=True,null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username  # You can choose how to represent the user

    # Add any additional methods or custom logic here
