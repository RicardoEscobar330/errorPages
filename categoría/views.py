from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Categoria
from .forms import categoriaForm

#Método que devuelve el JSON
def lista_categoria(request):
    #Obtener todas las instancias del objeto de la base de datos.
    categorias = Categoria.objects.all()

    #Construir una variable en formato de diccionario
    #Porque el JSONResponse lo requiere.
    data = [
        {
            #Objeto Producto construido al aire
            'nombre': p.nombre,
            'imagen': p.imagen
        }
        for p in categorias
    ]

    #Devolver la respuesta en JSON
    return JsonResponse(data, safe=False)

#Función para mandar a la vista del formulario
def agregar_categoria(request):
    #Averiguar si estamos teniendo una respuesta de form
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('verC') #Redirige a la lista de productos.
    #Pintar un formulario vacío
    else:
        form = categoriaForm()
    return render(request, 'agregarC.html', {'form': form})

def cards_categorias(request):
    return render(request, 'cards.html', status=200)