# Generated by Django 3.2.12 on 2022-06-29 01:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0012_auto_20220629_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2022, 8, 28, 1, 48, 29, 863711)),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2022, 6, 29, 1, 48, 29, 863697)),
        ),
    ]
