# Generated by Django 3.2.12 on 2022-05-11 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=' ', max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=' ', max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('backlog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlog.backlog')),
            ],
        ),
    ]
