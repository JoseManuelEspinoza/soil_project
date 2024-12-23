# Generated by Django 3.1.12 on 2024-12-21 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultivos', '0002_remove_cultivo_conductividad_min'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultivo',
            name='conductividad_min',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='fosforo_max',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='fosforo_min',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='nitrogeno_max',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='nitrogeno_min',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='nombre_cultivo',
            field=models.CharField(default='sensor', max_length=50),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='ph_max',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='ph_min',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='potasio_max',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='potasio_min',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cultivo',
            name='conductividad_max',
            field=models.FloatField(default=0),
        ),
    ]
