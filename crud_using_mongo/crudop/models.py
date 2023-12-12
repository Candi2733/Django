from djongo import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class User(BaseModel):
    employeeID = models.IntegerField(primary_key=True)
    employeeName = models.CharField(max_length=30)
    dob = models.DateField(null=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=320, unique=True)
    phone = models.CharField(max_length=10, unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

class Department(BaseModel):
    departmentID = models.IntegerField(primary_key=True)
    departmentName = models.CharField(max_length=20, unique=True)
