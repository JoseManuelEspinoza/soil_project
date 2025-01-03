from django.urls import path
from .views import createDatoSuelo, listDatoSuelo, editDatoSuelo, deleteDatoSuelo, searchDatoSuelo
urlpatterns = [
    path('crear/',createDatoSuelo,name='createDatoSuelo'),
    path('list/',listDatoSuelo,name='listDatoSuelo'),
    path('edit/<str:id>/',editDatoSuelo,name='editDatoSuelo'),
    path('delete/<str:id>/',deleteDatoSuelo,name='deleteDatoSuelo'),
    path('search/',searchDatoSuelo,name='searchDatoSuelo')
]
