from django.urls import path
from authentication import views
urlpatterns = [
    path('', views.home,name="home"),
    path('about', views.about,name="about"),
    path('signup', views.registerUser,name="registerUser"),
    path('login', views.loginUser,name="login"),
    path('logout', views.logoutUser,name="logout"),
]