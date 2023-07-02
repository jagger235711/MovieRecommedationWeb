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
from django.contrib.auth import views as auth_views
from django.urls import path

from userWeb import views as userWeb_views

app_name = "userWeb"
urlpatterns = [
    path('index/', userWeb_views.IndexView.as_view(), name="index"),
    path('admin/', userWeb_views.admin, name='admin'),
    path('movie/', userWeb_views.MovieView.as_view(), name="movie"),
    path('user/', userWeb_views.UserView.as_view(), name="user"),
    # 继承自模板
    path('register/', userWeb_views.RegisterView.as_view(), name='register'),
    path('logout/', userWeb_views.MyLogoutView.as_view(), name='logout'),
    path('login/', userWeb_views.MyLoginView.as_view(), name='login'),

    path('password_reset/', userWeb_views.MyPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
