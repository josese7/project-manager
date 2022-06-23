# Generated by Django 3.2.12 on 2022-06-10 00:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backlog', '0003_alter_backlog_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='comentario',
            field=models.TextField(blank=True, default=' ', null=True),
        ),
        migrations.AddField(
            model_name='userstory',
            name='estado',
            field=models.PositiveIntegerField(choices=[(2, 'Pendiente'), (1, 'Asignado'), (0, 'Finalizado')], default=2),
        ),
        migrations.AddField(
            model_name='userstory',
            name='usuarios',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]