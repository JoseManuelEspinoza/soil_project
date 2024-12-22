from djongo import models
from bson import ObjectId

class Sensor(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)  # <--- clave
    nombre = models.CharField(max_length=50, default='Sin nombre')
    tipo = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    precision = models.FloatField()

    def __str__(self):
        return self.nombre
