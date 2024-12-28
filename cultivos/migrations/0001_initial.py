# Generated by Django 3.1.12 on 2024-12-28 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cultivo', models.CharField(max_length=50)),
                ('ph_min', models.FloatField()),
                ('ph_max', models.FloatField()),
                ('fosforo_min', models.FloatField()),
                ('fosforo_max', models.FloatField()),
                ('potasio_min', models.FloatField()),
                ('potasio_max', models.FloatField()),
                ('nitrogeno_min', models.FloatField()),
                ('nitrogeno_max', models.FloatField()),
                ('conductividad_min', models.FloatField()),
                ('conductividad_max', models.FloatField()),
            ],
        ),
    ]
