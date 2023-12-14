import json
from django.http.response import JsonResponse
from .models import Outlet, Delivery
from .serializers import OutletSerializer, DeliverySerializer
from django.contrib.gis.geos import Point, GEOSGeometry

# Create your views here.
def index(request):
    return JsonResponse({'message' : 'Welcome to our page'})

def get_outlet_details(request):
    try:
        if request.method == 'GET':
            try:
                outlets = Outlet.objects.all()
                outlet = OutletSerializer(outlets, many = True)
                return JsonResponse(outlet.data, safe = False, status = 200)
            except Exception as e:
                return JsonResponse({'error' : str(e)}, status = 400)
        elif request.method == 'POST':
            try:
                outlet_data = json.loads(request.body)
                outlet_id = outlet_data.get('outlet_id')
                name = outlet_data.get('name')
                lat = outlet_data.get('lat')
                long = outlet_data.get('long')
                polygon_values = outlet_data.get('polygon')
                location = Point(lat, long, srid=4326)
                
                existing_outlet = Outlet.objects.filter(outlet_id=outlet_id).first()
                if existing_outlet:
                    return JsonResponse({'error' : 'Outlet data already exists'}, status = 400)
                try:
                    polygon = GEOSGeometry('MULTIPOLYGON ((%s))' %polygon_values, srid = 4326)
                    outlet = Outlet.objects.create(
                        outlet_id = outlet_id,
                        name = name,
                        lat = lat,
                        long = long,
                        area_covered = polygon,
                        location = location
                    )
                    outlet.save()
                    return JsonResponse({'message' : 'Outlet added successsfully'}, status = 200)
                except Exception as e:
                    return JsonResponse({'error' : str(e)}, status = 400)
            except Exception as e:
                return JsonResponse({'error' : str(e)}, status = 400)
        return JsonResponse({'error' : 'Method not allowed'}, status = 400)
    except Exception as e:
        return JsonResponse({'error' : str(e)}, status = 400)
    
def get_delivery_details(request):
    try:
        if request.method == 'GET':
            try:
                deliveries = Delivery.objects.all()
                delivery = DeliverySerializer(deliveries, many = True)
                return JsonResponse(delivery.data, safe = False, status = 200)
            except Exception as e:
                return JsonResponse({'error' : str(e)}, status = 400)
        elif request.method == 'POST':
            try:
                delivery_data = json.loads(request.body)
                delivery_id = delivery_data.get('delivery_id')
                is_polygon = delivery_data.get('is_polygon')
                polygon_area = delivery_data.get('polygon_area')
                radius = delivery_data.get('radius')
                outlet_id = delivery_data.get('outlet_id')

                existing_delivery = Delivery.objects.filter(delivery_id=delivery_id).first()
                if existing_delivery:
                    return JsonResponse({'error' : 'Delivery data already exists'}, status = 400)
                try:
                    if is_polygon == 1:
                        polygon = GEOSGeometry('POLYGON ((%s))' %polygon_area, srid = 4326)
                        delivery = Delivery.objects.create(
                            delivery_id = delivery_id,
                            is_polygon = is_polygon,
                            polygon_area = polygon,
                            outlet = Outlet.objects.get(outlet_id=outlet_id),
                            radius = radius
                        )
                    else:
                        delivery = Delivery.objects.create(
                            delivery_id = delivery_id,
                            is_polygon = is_polygon,
                            radius = radius,
                            outlet = Outlet.objects.get(outlet_id=outlet_id)
                        )
                    delivery.save()
                    return JsonResponse({'message' : 'Delivery added successsfully'}, status = 200)
                except Exception as e:
                    return JsonResponse({'error' : str(e)}, status = 400)
            except Exception as e:
                return JsonResponse({'error' : str(e)}, status = 400)
        return JsonResponse({'error' : 'Method not allowed'}, status = 400)
    except Exception as e:
        return JsonResponse({'error' : str(e)}, status = 400)