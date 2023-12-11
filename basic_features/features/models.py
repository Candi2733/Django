from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class User(BaseModel):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=10)
    dob = models.DateField(null=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=320, unique=True)
    phone = models.CharField(max_length=10, unique=True)