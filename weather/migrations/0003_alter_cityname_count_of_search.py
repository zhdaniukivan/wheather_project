# Generated by Django 5.0.7 on 2024-07-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_alter_userslastsearch_city_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityname',
            name='count_of_search',
            field=models.IntegerField(null=True),
        ),
    ]
