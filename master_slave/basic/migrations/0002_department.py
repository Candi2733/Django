# Generated by Django 4.1.13 on 2023-12-13 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('departmentID', models.IntegerField(primary_key=True, serialize=False)),
                ('departmentName', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
