from django.urls import URLPattern, path
from .views import home, componentes, formulario, ubicacion, terminos, productos

urlpatterns = [
    path('', home, name="home"),
    path('productos/', componentes, name="productos"),
    path('formulario/', formulario, name="formulario"),
    path('ubicacion/', ubicacion, name="ubicacion"),
    path('terminos/', terminos, name="terminos"),
    path('lista/', productos, name="lista"),
]