from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('file_upload', views.file_upload, name='sign_up'),
]