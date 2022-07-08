from django.urls import URLPattern, path
from .views import home, componentes, formulario, ubicacion, terminos, pago

urlpatterns = [
    path('', home, name="home"),
    path('productos/', componentes, name="productos"),
    path('formulario/', formulario, name="formulario"),
    path('ubicacion/', ubicacion, name="ubicacion"),
    path('terminos/', terminos, name="terminos"),
    path('pagar/', pago, name="pago"),

]