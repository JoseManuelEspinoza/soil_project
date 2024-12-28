from djongo import models  # Para trabajar con MongoDB y djongo
from bson import ObjectId
from dispositivos.models import Dispositivo

class DatoSuelo(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)  # Identificador único para el dato del suelo
    nombre = models.CharField(max_length=50)  # Nombre del dato
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha del dato
    nitrogeno = models.FloatField()
    potasio = models.FloatField()
    fosforo = models.FloatField()
    ph = models.FloatField()
    conductividad = models.FloatField()
    ubicacion = models.CharField(max_length=100)  # Ubicación del dispositivo
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name="datos_suelo", to_field="id")

    def __str__(self):
        return f"Dato de Suelo de {self.dispositivo.nombre} - {self.fecha}"
 