from django.shortcuts import render, HttpResponse, redirect
from .Carrito import Carrito
from .models import Producto

# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def componentes(request):
    productos = Producto.objects.all()
    return render(request, 'core/componentes.html', {'productos':productos})

def formulario(request):
    return render(request, 'core/formulario.html')

def terminos(request):
    return render(request, 'core/terminos.html')

def ubicacion(request):
    return render(request, 'core/ubicacion.html')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("productos")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("productos")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("productos")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("productos")


