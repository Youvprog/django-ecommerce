from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
     path('', views.login_user, name="login-user"),
     path('register', views.sign_up_user, name="register"),
     path('logout', LogoutView.as_view(next_page='login-user'), name="logout")
]
