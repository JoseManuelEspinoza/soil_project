from django.urls import path
from . import views

urlpatterns = [
    path('crear/',views.createCultivo,name='createCultivo'),
    path('list/',views.listCultivo, name='listCultivo'),
    path('',views.listCultivo, name='listCultivo'),
    path('edit/<int:id>/',views.editCultivo,name='editCultivo'),
    path('delete/<int:id>/',views.deleteCultivo,name='deleteCultivo'),
    path('search/',views.searchCultivo,name='searchCultivo')
]

