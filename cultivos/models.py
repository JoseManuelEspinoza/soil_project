from django.db import models

class Cultivo(models.Model):
    nombre_cultivo = models.CharField(max_length=50,default='sensor')
    ph_min = models.FloatField(default=0)
    ph_max = models.FloatField(default=0)
    fosforo_min = models.FloatField(default=0)
    fosforo_max = models.FloatField(default=0)
    potasio_min = models.FloatField(default=0)
    potasio_max = models.FloatField(default=0)
    nitrogeno_min = models.FloatField(default=0)
    nitrogeno_max = models.FloatField(default=0)  # Corregido
    conductividad_min = models.FloatField(default=0)
    conductividad_max = models.FloatField(default=0)

    def __str__(self):
        return self.nombre_cultivo
