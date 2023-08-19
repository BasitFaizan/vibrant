from django.urls import include, path
from authentication import views
urlpatterns = [
    path('<uuid:projectId>', views.explore,name="explore"),
    path('projectBlog/<uuid:projectBlogId>', views.view_project_blog,name="view_project_blog"),
]