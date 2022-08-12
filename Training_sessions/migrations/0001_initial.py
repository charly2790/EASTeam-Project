# Generated by Django 4.0.4 on 2022-07-31 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rpe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Training_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Tipo de Entrenamiento',
                'verbose_name_plural': 'Tipos de Entrenamiento',
            },
        ),
        migrations.CreateModel(
            name='Training_session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_assign', models.DateTimeField()),
                ('target', models.TextField()),
                ('training', models.TextField()),
                ('distance', models.FloatField()),
                ('time', models.TimeField()),
                ('done', models.BooleanField(default=False)),
                ('url', models.URLField()),
                ('rpe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Training_sessions.rpe')),
                ('tr_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Training_sessions.training_type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
