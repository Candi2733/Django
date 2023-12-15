import json
from django.http.response import JsonResponse
from .models import Outlet, Delivery
from .serializers import OutletSerializer
from django.contrib.gis.geos import Point, GEOSGeometry
from .functions import check_if_delivery, check_nearby_outlet

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
                data = []
                for deli in deliveries:
                    delivery = {
                        "delivery_id" : deli.delivery_id,
                        "is_polygon" : deli.is_polygon,
                        "polygon_area" : json.loads(deli.polygon_area.geojson),
                        "radius" : deli.radius,
                        "outlet_id" : deli.outlet.outlet_id
                    }
                    data.append(delivery)
                return JsonResponse(data, safe = False, status = 200)
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
    
def check_area_under_outlet(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            point_x = data.get('lat')
            point_y = data.get('long')
            point = Point(point_x, point_y, srid=4326)
            outlets = Outlet.objects.filter(area_covered__contains = point)
            data = []
            for out in outlets:
                outlet = {
                            "outlet_id" : out.outlet_id
                        }
                data.append(outlet)
            return JsonResponse(data, safe= False, status = 200)
        else:
            return JsonResponse({'error' : 'Method not allowed'}, status = 400)
    except Exception as e:
        return JsonResponse({'error' : str(e)}, status = 400)
    
def check_area_under_delivery(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            point_x = data.get('lat')
            point_y = data.get('long')
            point = Point(point_x, point_y, srid=4326)
            deliveries = Delivery.objects.filter(polygon_area__contains = point)
            data = []
            for deli in deliveries:
                delivery = {
                            "delivery_id" : deli.delivery_id,
                            "outlet_id" : deli.outlet.outlet_id
                        }
                data.append(delivery)
            return JsonResponse(data, safe= False, status = 200)
        else:
            return JsonResponse({'error' : 'Method not allowed'}, status = 400)
    except Exception as e:
        return JsonResponse({'error' : str(e)}, status = 400)
    
def delivery_possible(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            point_x = data.get('lat')
            point_y = data.get('long')
            point = Point(point_x, point_y, srid=4326)
            is_delivery_possible = check_if_delivery(point)
            # print(is_delivery_possible, 'sfusiiiiiiiiiiiiiii')
            if is_delivery_possible:
                delivery_details = Delivery.objects.filter(delivery_id = is_delivery_possible).first()
                delivery = {
                        "delivery_id" : delivery_details.delivery_id,
                        "is_polygon" : delivery_details.is_polygon,
                        "polygon_area" : json.loads(delivery_details.polygon_area.geojson),
                        "radius" : delivery_details.radius,
                        "outlet_id" : delivery_details.outlet.outlet_id,
                        "outlet_name" : delivery_details.outlet.name,
                        "location" : str(delivery_details.outlet.lat) + str(delivery_details.outlet.long),
                    }
                return JsonResponse(delivery, safe=False, status = 200)
            else:
                is_outlet_nearby = check_nearby_outlet(point)
                return is_outlet_nearby
        else:
            return JsonResponse({'error' : 'Method not allowed'}, status = 400)
    except Exception as e:
        return JsonResponse({'error' : str(e)}, status = 400)