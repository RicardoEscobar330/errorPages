from django.urls import path
from .views import * 

urlpatterns = [
    path('json/', cards_categorias, name='cardCategorias'),
    path('registrar/', agregar_categoria, name='agregarC'),
    path('api/get/', lista_categoria, name='verC')
]