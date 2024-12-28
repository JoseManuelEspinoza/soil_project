from django import forms
from .models import Cultivo

class CultivoForm(forms.ModelForm):
    class Meta:
        model = Cultivo
        fields = '__all__'
        widgets = {
            'nombre_cultivo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingresa el nombre del cultivo'
            }),
            'ph_min': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'pH mínimo'
            }),
            'ph_max': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'pH máximo'
            }),
            'fosforo_min': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fósforo mínimo'
            }),
            'fosforo_max': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fósforo máximo'
            }),
            'potasio_min': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Potasio mínimo'
            }),
            'potasio_max': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Potasio máximo'
            }),
            'nitrogeno_min': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nitrógeno mínimo'
            }),
            'nitrogeno_max': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nitrógeno máximo'
            }),
            'conductividad_min': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Conductividad mínima'
            }),
            'conductividad_max': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Conductividad máxima'
            }),
        }
