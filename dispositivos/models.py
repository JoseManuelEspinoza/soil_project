from djongo import models  # Asegúrate de usar djongo si estás trabajando con MongoDB
from bson import ObjectId
from sensores.models import Sensor

# Modelos

class SensorEmbebido(models.Model):
    id_sensor = models.ObjectIdField()
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    precision = models.FloatField()

    class Meta:
        abstract = True
        
class Dispositivo(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    sensores = models.ArrayField(model_container=SensorEmbebido)

    def __str__(self):
        return self.nombre
