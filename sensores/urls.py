
from django.urls import path
from . import views

urlpatterns = [
    path('crear/',views.createSensor,name='createSensor'),
    path('list/',views.listSensor,name='listSensor'),
    path('edit/<str:id>/',views.editSensor,name='editSensor'),
    path('delete/<str:id>/',views.deleteSensor,name='deleteSensor'),
    path('search/',views.searchSensor,name='searchSensor')
]

