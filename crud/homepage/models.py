from django.db import models

class User(models.Model):
    email = models.EmailField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=255)
    updated_timestamp = models.TimeField(auto_now=True)