# Generated by Django 3.2.12 on 2022-06-25 00:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0008_auto_20220622_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2022, 8, 24, 0, 10, 56, 221651)),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2022, 6, 25, 0, 10, 56, 221639)),
        ),
    ]
