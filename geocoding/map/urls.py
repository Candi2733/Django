from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('outlet', views.get_outlet_details, name='outlet'),
    path('delivery', views.get_delivery_details, name='delivery'),
    path('find_outlet', views.check_area_under_outlet, name = 'find_outlet'),
    path('find_delivery', views.check_area_under_delivery, name = 'find_delivery'),
    path('delivery_possible', views.delivery_possible, name='delivery_possible')
]