from django.urls import path
from . import views

urlpatterns = [
    path('crear/',views.createCultivo,name='createCultivo'),
    path('list/',views.listCultivo, name='listcultivos')

]

