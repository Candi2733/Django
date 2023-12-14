# Generated by Django 4.1.13 on 2023-12-14 11:52

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Outlet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('outlet_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('area_covered', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('delivery_id', models.IntegerField(unique=True)),
                ('is_polygon', models.BooleanField()),
                ('polygon_area', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('radius', models.IntegerField()),
                ('outlet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.outlet')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
