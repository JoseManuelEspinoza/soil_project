from django import forms
from .models import Sensor

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del sensor'
            }),
            'tipo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el tipo de sensor'
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el modelo del sensor'
            }),
            'precision': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la precisión del sensor'
            }),
        }
        labels = {
            'nombre': 'Nombre del Sensor',
            'tipo': 'Tipo',
            'modelo': 'Modelo',
            'precision': 'Precisión',
        }
