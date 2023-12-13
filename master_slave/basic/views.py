from django.http import JsonResponse
from .models import User
from .serializers import EmployeeSerializer
from rest_framework.parsers import JSONParser

# Create your views here.

def index(request):
    return JsonResponse({'message': 'homepage'}, status = 200)

def employee(request):
    try:
        if request.method == 'GET':
            try:
                employee = User.objects.all()
                employees_serializer = EmployeeSerializer(employee, many = True)

                return JsonResponse(employees_serializer.data, safe = False, status = 200)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status = 400)
        
        elif request.method == 'POST':
            try:
                employee_data=JSONParser().parse(request)
                employees_serializer=EmployeeSerializer(data=employee_data)
                if employees_serializer.is_valid():
                    employees_serializer.save()
                    return JsonResponse({"message": "Added Successfully"}, safe = False, status = 200)
                return JsonResponse(employees_serializer.errors, status=400)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status = 400)

        elif request.method == 'PUT':
            try:
                employee_data=JSONParser().parse(request)
                employee=User.objects.get(employeeID=employee_data['employeeID'])
                employees_serializer=EmployeeSerializer(employee,data=employee_data)

                if employees_serializer.is_valid():
                    employees_serializer.save()
                    return JsonResponse({"message" : "Updated Successfully"}, safe = False, status = 200)
                
                return JsonResponse({"message" : "Failed to Update"}, status = 500)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status = 400)
        
        elif request.method == 'DELETE':
            try:
                employee_data = JSONParser().parse(request)
                employee_id = employee_data.get('employeeID')

                try:
                    employee = User.objects.get(employeeID=employee_id)
                    employee.delete()
                    return JsonResponse({"message" : "Deleted Successfully"}, safe=False, status=200)
                except Exception as e:
                    return JsonResponse({'error': str(e)}, status=400)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)