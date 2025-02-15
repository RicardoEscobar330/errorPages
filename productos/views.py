from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto
from .forms import productoForm

#Método que devuelve el JSON
def lista_productos(request):
    #Obtener todas las instancias del objeto de la base de datos.
    productos = Producto.objects.all()

    #Construir una variable en formato de diccionario
    #Porque el JSONResponse lo requiere.
    data = [
        {
            #Objeto Producto construido al aire
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]

    #Devolver la respuesta en JSON
    return JsonResponse(data, safe=False)

#Función para mandar a la vista del formulario
def agregar_producto(request):
    #Averiguar si estamos teniendo una respuesta de form
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver') #Redirige a la lista de productos.
    #Pintar un formulario vacío
    else:
        form = productoForm()
    return render(request, 'agregar.html', {'form': form})