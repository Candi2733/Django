from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('user_profile', views.user_profile, name='logout'),
    path('update_user', views.update_user, name='logout'),
]