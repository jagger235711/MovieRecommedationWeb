"""MovieRecommedationWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from userWeb import views as userWeb_views
app_name = "userWeb"
urlpatterns = [
    path('index/', userWeb_views.IndexView.as_view(), name="index"),
    path('admin/', userWeb_views.admin, name='admin'),
    path('movie/', userWeb_views.MovieView.as_view(), name="movie"),
    path('user/', userWeb_views.UserView.as_view(), name="user"),
    # 继承自模板

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('register/', auth_views., name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
