# Generated by Django 5.0.7 on 2024-07-17 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userslastsearch',
            name='city_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='weather.cityname'),
        ),
    ]
