from django import forms
from .models import Cultivo

class CultivoForm(forms.ModelForm):
    class Meta:
        model = Cultivo
        fields = '__all__'