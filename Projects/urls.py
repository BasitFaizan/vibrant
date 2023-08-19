from django.urls import include, path
from authentication import views
urlpatterns = [
    path('<uuid:projectId>', views.explore,name="explore"),
]