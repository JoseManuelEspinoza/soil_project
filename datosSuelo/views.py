from django.shortcuts import render, redirect
from .models import DatoSuelo
from dispositivos.models import Dispositivo
from bson import ObjectId

def createDatoSuelo(request):
    if request.method == 'POST':
        id = ObjectId()
        nitrogeno = float(request.POST.get('nitrogeno'))
        potasio = float(request.POST.get('potasio'))
        fosforo = float(request.POST.get('fosforo'))
        ph = float(request.POST.get('ph'))
        conductividad = float(request.POST.get('conductividad'))
        dispositivo_id = request.POST.get('dispositivo')  # ID del dispositivo

        # Obtener el dispositivo relacionado
        dispositivo = Dispositivo.objects.get(id=ObjectId(dispositivo_id))

        # Crear un nuevo dato de suelo
        DatoSuelo.objects.create(
            id=id,
            nitrogeno=nitrogeno,
            potasio=potasio,
            fosforo=fosforo,
            ph=ph,
            conductividad=conductividad,
            dispositivo=dispositivo
        )
        return redirect('listDatoSuelo')

    # Obtener todos los dispositivos
    dispositivos = Dispositivo.objects.all()
    return render(request, 'datoSuelo/createDatoSuelo.html', {'dispositivos': dispositivos})
def listDatoSuelo(request):
    datos_suelo = DatoSuelo.objects.all()  # Obtiene todos los datos de suelo
    return render(request, 'datoSuelo/listDatoSuelo.html', {'datos_suelo': datos_suelo})

def editDatoSuelo(request, id):
    dato_suelo = DatoSuelo.objects.get(id=ObjectId(id))  # Obtiene el dato de suelo por su ID

    if request.method == 'POST':
        # Actualiza los campos del dato de suelo
        dato_suelo.nitrogeno = float(request.POST.get('nitrogeno'))
        dato_suelo.potasio = float(request.POST.get('potasio'))
        dato_suelo.fosforo = float(request.POST.get('fosforo'))
        dato_suelo.ph = float(request.POST.get('ph'))
        dato_suelo.conductividad = float(request.POST.get('conductividad'))
        dispositivo_id = request.POST.get('dispositivo')  # ID del dispositivo

        # Obtener el dispositivo relacionado
        dispositivo = Dispositivo.objects.get(id=ObjectId(dispositivo_id))
        dato_suelo.dispositivo = dispositivo

        # Guarda los cambios
        dato_suelo.save()
        return redirect('listDatoSuelo')

    # Obtener todos los dispositivos
    dispositivos = Dispositivo.objects.all()
    return render(request, 'datoSuelo/editDatoSuelo.html', {'dato_suelo': dato_suelo, 'dispositivos': dispositivos})
def deleteDatoSuelo(request, id):
    dato_suelo = DatoSuelo.objects.get(id=ObjectId(id))  # Obtiene el dato de suelo por su ID
    dato_suelo.delete()  # Elimina el dato de suelo
    return redirect('listDatoSuelo')