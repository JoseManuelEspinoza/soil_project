from django.db import models

class Cultivo(models.Model):
    nombre_cultivo = models.CharField(max_length=50)
    ph_min = models.FloatField()
    ph_max = models.FloatField()
    fosforo_min = models.FloatField()
    fosforo_max = models.FloatField()
    potasio_min = models.FloatField()
    potasio_max = models.FloatField()
    nitrogeno_min = models.FloatField()
    nitrogeno_max = models.FloatField()  # Corregido
    conductividad_min = models.FloatField()
    conductividad_max = models.FloatField()

    def __str__(self):
        return self.nombre_cultivo
