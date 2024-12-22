from django.shortcuts import render,redirect,get_object_or_404
from .models import Sensor
from .forms import SensorForm
from bson import ObjectId

# Create your views here.
def createSensor(request):
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listSensor')
    else:
        form = SensorForm()
        return render(request,'sensores/createSensor.html',{
            'form':form
        })

def listSensor(request):
    sensores=Sensor.objects.all()
    return render(request,'sensores/listSensor.html',
    {'sensores':sensores})

def editSensor(request,id):
    object_id = ObjectId(id)
    sensor = get_object_or_404(Sensor, id=object_id)
    if request.method == 'POST':
        form=SensorForm(request.POST,instance=sensor)
        if form.is_valid():
            form.save()
            return redirect('listSensor')
    else:
        form=SensorForm(instance=sensor)
        return render(request,'sensores/editSensor.html',
        {'form':form})
def deleteSensor(request,id):
    object_id=ObjectId(id)
    sensor=Sensor.objects.get(id=object_id)
    sensor.delete()
    return redirect('listSensor')

def searchSensor(request):
    query=request.GET.get('q','')
    sensores=Sensor.objects.filter(nombre__icontains=query)
    return render (request,'sensores/sensores_table.html',
    {'sensores':sensores})