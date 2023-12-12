from django.http import JsonResponse
from django.shortcuts import render
from .models import User, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
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

def department(request):
    try:
        if request.method == 'GET':
            try:                    
                departments = Department.objects.all()
                department_serializer = DepartmentSerializer(departments, many = True) 
                return JsonResponse(department_serializer.data, safe = False, status = 200)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status = 400)
            
        elif request.method == 'POST':
            try:
                department_data=JSONParser().parse(request)
                department_serializer=DepartmentSerializer(data=department_data)
                if department_serializer.is_valid():
                    department_serializer.save()
                    return JsonResponse({"messae" : "Added Successfully"}, safe = False, status = 200)
                return JsonResponse(department_serializer.errors, status=400)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status = 400)

        elif request.method == 'PUT':
            try:
                department_data=JSONParser().parse(request)
                department_id = department_data.get('departmentID')
                department = Department.objects.get(departmentID=department_id)
                department_serializer=DepartmentSerializer(department,data=department_data)

                if department_serializer.is_valid():
                    department_serializer.save()
                    return JsonResponse({"message" : "Updated Successfully"}, status = 200)
                
                return JsonResponse({"message" : "Failed to Update"}, status = 500)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status = 400)
        
        elif request.method == 'DELETE':
            try:
                department_data = JSONParser().parse(request)
                dept_id = department_data.get('departmentID')  # Assuming the key is 'departmentID'
                dept = Department.objects.get(departmentID=dept_id)
                dept.delete()

                return JsonResponse({"message" : "Deleted Successfully"}, status=200)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)