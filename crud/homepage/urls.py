from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_user', views.add_user, name='add_user'),
    path('edit_user/<str:emailid>', views.edit_user, name='edit_user'),
    path('save_user', views.save_user, name='save_user'),
    path('delete_user/<str:emailid>', views.delete_user, name='delete_user'),
    path('check_email', views.check_email, name='check_email')
]