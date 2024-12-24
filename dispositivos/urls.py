from django.urls import path
from .views import createDispositivo,listDispositivo,searchDispositivo, editDispositivo, deleteDispositivo

urlpatterns = [
    path('crear/', createDispositivo, name='createDispositivo'),
    path('list/',listDispositivo,name='listDispositivo'),
    path('edit/<str:id>',editDispositivo,name='editDispositivo'),
    path('delete/<str:id>',deleteDispositivo,name='deleteDispositivo'),
    path('search/',searchDispositivo,name='searchDispositivo')
]
