from django.shortcuts import render, redirect
from .forms import CultivoForm
from .models import Cultivo

# Create your views here.
def createCultivo(request):
    if request.method == 'POST':
        form = CultivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listcultivos')  # Redirigir a una vista después de guardar
    else:
        form = CultivoForm()
        return render(request, 'cultivos/createCultivo.html', {'form': form})

def listCultivo(request):
    cultivos=Cultivo.objects.all()
    return render(request,'cultivos/listCultivo.html',
    {'cultivos':cultivos})