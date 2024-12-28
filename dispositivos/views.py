from django.shortcuts import render, redirect, get_object_or_404
from .models import Dispositivo,SensorEmbebido
from sensores.models import Sensor
from bson import ObjectId
from django.contrib import messages
# Create your views here.
# dispositivos/views.py
def createDispositivo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        sensores_list = request.POST.getlist('sensores')
        # Convertir a ObjectId y obtener QuerySet
        sensores_seleccionados = Sensor.objects.filter(
            id__in=[ObjectId(s) for s in sensores_list]
        )

        # Armar la lista embebida
        sensores_embebidos = []
        for sensor in sensores_seleccionados:
            sensores_embebidos.append({
                'id_sensor': sensor.id,
                'nombre': sensor.nombre,
                'tipo': sensor.tipo,
                'precision': sensor.precision,
            })

        # Guardar
        Dispositivo.objects.create(
            nombre=nombre,
            tipo=tipo,
            sensores=sensores_embebidos
        )
        messages.success(request, 'El dispositivo se ha guardado correctamente.')  # Mensaje de éxito
        return redirect('listDispositivo')

    # GET
    sensores = Sensor.objects.all()
    return render(request, 'dispositivos/createDispositivo.html', {'sensores': sensores})


def listDispositivo(request):
    dispositivos=Dispositivo.objects.all()
    return render(request,'dispositivos/listDispositivo.html',
    {'dispositivos':dispositivos})


def editDispositivo(request, id):
    dispositivo = get_object_or_404(Dispositivo, id=ObjectId(id))

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        sensores_list = request.POST.getlist('sensores')

        sensores_seleccionados = Sensor.objects.filter(
            id__in=[ObjectId(s) for s in sensores_list]
        )
        sensores_embebidos = [
            {
                'id_sensor': sensor.id,
                'nombre': sensor.nombre,
                'tipo': sensor.tipo,
                'precision': sensor.precision,
            }
            for sensor in sensores_seleccionados
        ]

        dispositivo.nombre = nombre
        dispositivo.tipo = tipo
        dispositivo.sensores = sensores_embebidos
        dispositivo.save()
        messages.success(request, 'El dispositivo se ha actualizado correctamente.')  # Mensaje de éxito

        return redirect('listDispositivo')

    sensores = Sensor.objects.all()
    sensores_seleccionados_ids = [sensor['id_sensor'] for sensor in dispositivo.sensores]

    return render(request, 'dispositivos/editDispositivo.html', {
        'dispositivo': dispositivo,
        'sensores': sensores,
        'sensores_seleccionados_ids': sensores_seleccionados_ids,
    })

def deleteDispositivo(request, id):
    try:
        dispositivo = get_object_or_404(Dispositivo, id=ObjectId(id))
        dispositivo.delete()
        messages.success(request, 'El dispositivo se ha eliminado correctamente.')
    except Exception as e:
        messages.error(request, f'Error al eliminar el dispositivo: {str(e)}')
    return redirect('listDispositivo')

def searchDispositivo(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda (vacío por defecto)
    
    if query:
        dispositivos = Dispositivo.objects.filter(nombre__icontains=query)  # Filtrar por búsqueda
    else:
        dispositivos = Dispositivo.objects.all()  # Retornar todos los dispositivos si no hay búsqueda
    
    return render(request, 'dispositivos/dispositivo_table.html', {
        'dispositivos': dispositivos
    })





