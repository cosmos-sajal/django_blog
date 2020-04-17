from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import register, profile

urlpatterns = [
    path('register/', register, name='user-register'),
    path('profile/', profile, name='user-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='user-logout')
]
