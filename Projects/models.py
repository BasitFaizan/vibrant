from django.db import models
from base.models import BaseModel
from authentication.models import customUser
from ckeditor.fields import RichTextField

# Create your models here.

class Projectcard(BaseModel):
    by_Created = models.ForeignKey(customUser,on_delete=models.CASCADE,related_name='by_created',blank=True,null=True)
    title = models.CharField(name='title',max_length=100)
    projectTitleImage = models.ImageField(name='projectTitleImage',upload_to='media/projectTitleImage')


class ProjectBlog(BaseModel):
    projectCateg = models.ForeignKey(Projectcard,on_delete=models.CASCADE,related_name='by_projectcard')
    authorName = models.ForeignKey(customUser, on_delete=models.CASCADE ,null=True )
    blogTitle = models.CharField(name='blogTitle',max_length=200)
    projectBlogImage = models.ImageField(name='projectTitleImage',upload_to='media/projectBlogImages')
    content = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.blogTitle