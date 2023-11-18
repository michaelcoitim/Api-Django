from rest_framework import serializers
from FirstApp.models import Departaments,Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departaments
        fields=('DepartmentId','DepartamentName')

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeestId','EmployeesName','Department','DateOfJoining','PhotoFileName')        