#
from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path(
        'user/register/', 
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        'login/', 
        views.LoginUser.as_view(),
        name='user-login',
    ),
    path(
        'user/logout/', 
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    path(
        'user/update/', 
        views.UpdatePasswordView.as_view(),
        name='user-update',
    ),
]