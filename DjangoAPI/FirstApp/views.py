from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from FirstApp.models import Departaments,Employees
from FirstApp.serializers import DepartmentSerializer, EmployeesSerializer

# Create your views here.

@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departaments.objects.all()
        departments_serializer = DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method =='POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("adicionado com sucesso!", safe=False)
        return JsonResponse("Erro ao adicionar",safe=False)
    elif request.method =='PUT':
        department_data = JSONParser().parse(request)
        department = Departaments.objects.get(DepartmentId = department_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Atualziado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar",safe=False)
    elif request.method =='DELETE':
        department = Departaments.objects.get(DepartmentId =id)
        department.delete()
        return JsonResponse("Deletado com sucesso", safe=False)