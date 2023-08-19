from django.db import models
from base.models import BaseModel
from authentication.models import customUser

# Create your models here.

class Projectcard(BaseModel):
    by_Created = models.ForeignKey(customUser,on_delete=models.CASCADE,related_name='by_created',blank=True,null=True)
    title = models.CharField(name='title',max_length=100)
    projectTitleImage = models.ImageField(name='projectTitleImage',upload_to='media/projectTitleImage')