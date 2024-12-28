from django.shortcuts import render, redirect,  get_object_or_404
from .forms import CultivoForm
from .models import Cultivo
from django.contrib import messages

def createCultivo(request):
    if request.method == 'POST':
        form = CultivoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El cultivo se ha guardado correctamente.')
            return redirect('listCultivo')  # Redirigir a la lista después de guardar
    else:
        form = CultivoForm()  # No se pasa ningún valor inicial
    return render(request, 'cultivos/createCultivo.html', {'form': form})


def listCultivo(request):
    cultivos=Cultivo.objects.all()
    return render(request,'cultivos/listCultivo.html',
    {'cultivos':cultivos})

def deleteCultivo(request,id):
    cultivo=Cultivo.objects.get(id=id)
    cultivo.delete()
    messages.success(request, 'El cultivo se ha eliminado correctamente.')  # Mensaje de éxito
    return redirect('listCultivo')

def editCultivo(request, id):
    cultivo = get_object_or_404(Cultivo, id=id)
    if request.method == 'POST':
        form = CultivoForm(request.POST, instance=cultivo)
        if form.is_valid():
            form.save()
            messages.success(request, 'El cultivo se ha actualizado correctamente.')  # Mensaje de éxito
            return redirect('listCultivo')  # Redirige a la lista para que se muestre el mensaje
    else:
        form = CultivoForm(instance=cultivo)
    return render(request, 'cultivos/editCultivo.html', {'form': form})
def searchCultivo(request):
    query=request.GET.get('q','')
    cultivos=Cultivo.objects.filter(nombre_cultivo__icontains=query)
    return render (request,'cultivos/cultivos_table.html',
    {'cultivos':cultivos})