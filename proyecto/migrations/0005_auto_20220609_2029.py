# Generated by Django 3.2.12 on 2022-06-10 00:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0004_auto_20220511_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2022, 8, 8, 20, 29, 18, 145428)),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2022, 6, 9, 20, 29, 18, 145428)),
        ),
    ]