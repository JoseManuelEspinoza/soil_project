# dispositivos/fields.py
from django import forms
from bson import ObjectId
from sensores.models import Sensor

class ObjectIdMultipleChoiceField(forms.ModelMultipleChoiceField):
    """
    Un campo que convierte los valores del POST (strings) en ObjectId 
    y luego hace la búsqueda con id__in=[ObjectId(...), ...].
    """

    def to_python(self, value):
        """
        Convierte cada valor de la lista en un ObjectId antes de validarlo.
        """
        if not value:
            return []
        try:
            return [ObjectId(v) for v in value]
        except Exception as e:
            raise forms.ValidationError(f"Ocurrió un problema convirtiendo a ObjectId: {e}")

    def validate(self, value):
        """
        Llama a la validación por defecto de ModelMultipleChoiceField.
        """
        return super().validate(value)

    def get_queryset(self):
        """
        Sobrescribe el queryset con todos los sensores.
        """
        return Sensor.objects.all()

    def clean(self, value):
        """
        Aplica `to_python`, luego filtra en la BD usando ObjectId.
        """
        oid_list = self.to_python(value)  # lista de ObjectId
        qs = self.get_queryset().filter(id__in=oid_list)
        self.run_validators(qs)
        if self.required and not qs:
            raise forms.ValidationError("Este campo es requerido.")
        return qs
