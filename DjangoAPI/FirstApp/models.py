from django.db import models

# Create your models here.

class Departaments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartamentName =models.CharField(max_length=500)

    class Employees(models.Model):
        EmployeeId = models.AutoField(primary_key=True)
        Employeename = models.CharField(max_length=500)
        Department = models.CharField(max_length=500)
        DateOfJoining = models.DateField()
        PhotoFileName = models.CharField(max_length=500)