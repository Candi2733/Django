from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('outlet', views.get_outlet_details, name='outlet'),
    path('delivery', views.get_delivery_details, name='delivery'),
]