# Generated by Django 3.1.12 on 2024-12-22 14:07

import bson.objectid
import dispositivos.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, default=bson.objectid.ObjectId, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('sensores', djongo.models.fields.ArrayField(model_container=dispositivos.models.SensorEmbebido)),
            ],
        ),
    ]
