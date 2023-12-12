from rest_framework import serializers
from .models import User, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['departmentID','departmentName']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['employeeID','employeeName','dob','email','phone', 'department']