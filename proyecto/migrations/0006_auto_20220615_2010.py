# Generated by Django 3.2.12 on 2022-06-16 00:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0005_auto_20220609_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2022, 8, 14, 20, 10, 43, 635359)),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2022, 6, 15, 20, 10, 43, 626362)),
        ),
    ]
