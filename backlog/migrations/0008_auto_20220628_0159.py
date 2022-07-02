# Generated by Django 3.2.12 on 2022-06-28 01:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0001_initial'),
        ('backlog', '0007_alter_comentario_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='sprint',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sprint.sprint'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2022, 6, 28, 1, 59, 24, 107360)),
        ),
    ]