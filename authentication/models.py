from django.db import models
from base.models import BaseModel
# Create your models here.
# Create your models here.

class User(BaseModel):
    username = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=8)
