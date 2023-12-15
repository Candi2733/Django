from django.contrib.gis.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class Outlet(BaseModel):
    outlet_id = models.IntegerField(unique = True)
    name = models.CharField(max_length = 20)
    location = models.PointField()
    lat = models.FloatField()
    long = models.FloatField()
    area_covered = models.MultiPolygonField()

class Delivery(BaseModel):
    delivery_id = models.IntegerField(unique = True)
    is_polygon = models.BooleanField()
    polygon_area = models.PolygonField(null = True)
    radius = models.IntegerField(null = True)
    outlet = models.ForeignKey('Outlet', on_delete = models.CASCADE)
    is_active = models.BooleanField(default = 1)