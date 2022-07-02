# Generated by Django 3.2.12 on 2022-06-29 01:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backlog', '0010_auto_20220629_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2022, 6, 29, 1, 48, 29, 866471)),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='backlog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlog.backlog'),
        ),
    ]