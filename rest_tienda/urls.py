from django.urls import path
from rest_tienda.views import detalle_productos, listar_productos

urlpatterns = [
    path('listar_productos', listar_productos, name="listar_productos"),
    path('detalle_productos/<id>', detalle_productos, name="detalle_productos"),

]