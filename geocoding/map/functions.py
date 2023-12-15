from .models import Delivery, Outlet
from django.http.response import JsonResponse
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance

def check_if_delivery(point):
    try:
        deliveries = Delivery.objects.filter(polygon_area__contains = point)
        if deliveries:
            return deliveries[0].delivery_id
        else:
            return False
    except Exception as e:
        return JsonResponse({'error' : str(e)}, status = 400)


def check_nearby_outlet(point):
    try:
        outlets = Outlet.objects.filter(location__distance_lte=(point, 0.09009)).annotate(distance=Distance('location', point)).order_by('distance')
        if outlets:
            data = []
            for i in outlets:
                outlet_details = {
                    "outlet_id": i.outlet_id,
                    "outlet_name": i.name,
                    "location": str(i.lat) + str(i.long),
                    "distance": i.distance*111.0
                }
                data.append(outlet_details)
            return JsonResponse(data, safe=False, status=200)
        else:
            return JsonResponse({'error': 'No outlets within 10 km distance detected'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
