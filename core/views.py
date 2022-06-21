from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def componentes(request):
    return render(request, 'core/componentes.html')

def formulario(request):
    return render(request, 'core/formulario.html')

def terminos(request):
    return render(request, 'core/terminos.html')

def ubicacion(request):
    return render(request, 'core/ubicacion.html')




