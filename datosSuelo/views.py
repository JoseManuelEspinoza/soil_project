from django.shortcuts import render, redirect, get_object_or_404
from .models import DatoSuelo
from dispositivos.models import Dispositivo
from bson import ObjectId
from django.contrib import messages

def createDatoSuelo(request):
    if request.method == 'POST':
        try:
            # Nuevos campos: nombre y ubicación
            nombre = request.POST.get('nombre')
            ubicacion = request.POST.get('ubicacion')
            nitrogeno = float(request.POST.get('nitrogeno'))
            potasio = float(request.POST.get('potasio'))
            fosforo = float(request.POST.get('fosforo'))
            ph = float(request.POST.get('ph'))
            conductividad = float(request.POST.get('conductividad'))
            dispositivo_id = request.POST.get('dispositivo')

            dispositivo = get_object_or_404(Dispositivo, id=ObjectId(dispositivo_id))
            DatoSuelo.objects.create(
                nombre=nombre,
                ubicacion=ubicacion,
                nitrogeno=nitrogeno,
                potasio=potasio,
                fosforo=fosforo,
                ph=ph,
                conductividad=conductividad,
                dispositivo=dispositivo
            )
            messages.success(request, "El dato de suelo se ha creado correctamente.")
        except Exception as e:
            messages.error(request, f"Error al crear el dato de suelo: {e}")
        return redirect('listDatoSuelo')

    dispositivos = Dispositivo.objects.all()
    return render(request, 'datoSuelo/createDatoSuelo.html', {'dispositivos': dispositivos})

def listDatoSuelo(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda
    if query:
        datos_suelo = DatoSuelo.objects.filter(dispositivo__nombre__icontains=query)
    else:
        datos_suelo = DatoSuelo.objects.all()
    return render(request, 'datoSuelo/listDatoSuelo.html', {'datos_suelo': datos_suelo, 'query': query})

def editDatoSuelo(request, id):
    dato_suelo = get_object_or_404(DatoSuelo, id=ObjectId(id))
    if request.method == 'POST':
        try:
            # Nuevos campos: nombre y ubicación
            dato_suelo.nombre = request.POST.get('nombre')
            dato_suelo.ubicacion = request.POST.get('ubicacion')
            dato_suelo.nitrogeno = float(request.POST.get('nitrogeno'))
            dato_suelo.potasio = float(request.POST.get('potasio'))
            dato_suelo.fosforo = float(request.POST.get('fosforo'))
            dato_suelo.ph = float(request.POST.get('ph'))
            dato_suelo.conductividad = float(request.POST.get('conductividad'))
            dispositivo_id = request.POST.get('dispositivo')

            dispositivo = get_object_or_404(Dispositivo, id=ObjectId(dispositivo_id))
            dato_suelo.dispositivo = dispositivo
            dato_suelo.save()
            messages.success(request, "El dato de suelo se ha actualizado correctamente.")
        except Exception as e:
            messages.error(request, f"Error al actualizar el dato de suelo: {e}")
        return redirect('listDatoSuelo')

    dispositivos = Dispositivo.objects.all()
    return render(request, 'datoSuelo/editDatoSuelo.html', {'dato_suelo': dato_suelo, 'dispositivos': dispositivos})

def deleteDatoSuelo(request, id):
    try:
        dato_suelo = get_object_or_404(DatoSuelo, id=ObjectId(id))
        dato_suelo.delete()
        messages.success(request, "El dato de suelo se ha eliminado correctamente.")
    except Exception as e:
        messages.error(request, f"Error al eliminar el dato de suelo: {e}")
    return redirect('listDatoSuelo')

def searchDatoSuelo(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda
    if query:
        # Buscar datos de suelo por el nombre
        datos_suelo = DatoSuelo.objects.filter(nombre__icontains=query)
    else:
        datos_suelo = DatoSuelo.objects.all()  # Mostrar todos si no hay término de búsqueda

    return render(request, 'datoSuelo/datosSuelo_table.html', {'datos_suelo': datos_suelo})
