from django.urls import URLPattern, path
from .views import home, componentes, formulario, ubicacion, terminos

urlpatterns = [
    path('', home, name="home"),
    path('', componentes, name="productos"),
    path('', formulario, name="formulario"),
    path('', ubicacion, name="ubicacion"),
    path('', terminos, name="terminos"),

]