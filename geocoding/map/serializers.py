from rest_framework import serializers
from .models import Outlet, Delivery

class OutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = ['outlet_id', 'name', 'location', 'lat', 'long', 'area_covered']

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['delivery_id','is_polygon','polygon_area','radius','outlet']