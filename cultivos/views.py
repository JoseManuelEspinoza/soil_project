from django.shortcuts import render, redirect,  get_object_or_404
from .forms import CultivoForm
from .models import Cultivo

# Create your views here.
def createCultivo(request):
    if request.method == 'POST':
        form = CultivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listCultivo')  # Redirigir a una vista después de guardar
    else:
        form = CultivoForm()
        return render(request, 'cultivos/createCultivo.html', {'form': form})

def listCultivo(request):
    cultivos=Cultivo.objects.all()
    return render(request,'cultivos/listCultivo.html',
    {'cultivos':cultivos})

def deleteCultivo(request,id):
    cultivo=Cultivo.objects.get(id=id)
    cultivo.delete()
    return redirect('listCultivo')

def editCultivo(request,id):
    cultivo=get_object_or_404(Cultivo,id=id)
    if request.method =='POST':
        form=CultivoForm(request.POST,instance=cultivo)
        if form.is_valid():
            form.save()
            return redirect('listCultivo')
    else:
        form=CultivoForm(instance=cultivo)
        return render(request,'cultivos/editCultivo.html',
        {'form':form})
def searchCultivo(request):
    query=request.GET.get('q','')
    cultivos=Cultivo.objects.filter(nombre_cultivo__icontains=query)
    return render (request,'cultivos/cultivos_table.html',
    {'cultivos':cultivos})