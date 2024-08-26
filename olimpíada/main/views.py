from rest_framework import viewsets
from .models import Producto, Pedido
from .serializers import ProductoSerializer, PedidoSerializer
from django.shortcuts import render


def index(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return render(request, 'index.html', {'productos': serializer.data})
