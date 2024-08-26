from rest_framework import viewsets
from .models import Producto, Pedido
from .serializers import ProductoSerializer, PedidoSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

#@login_required(login_url='login')
def home(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return render(request, 'index.html', {'productos': serializer.data})

#@login_required(login_url='login')
def productos(request):
    productos = Producto.objects.order_by('codigo')
    serializer = ProductoSerializer(productos, many=True)
    return render(request, 'productos.html', {'productos': serializer.data})

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def pedido(request):
    productos = Producto.objects.order_by('codigo')
    serializer = ProductoSerializer(productos, many=True)
    return render(request, 'pedido.html', {'productos': serializer.data})

def agregarAlCarrito(request, id):
    producto = Producto.objects.get(pk=id)
    pedido = Pedido.objects.create(cliente=request.user.cliente)
    pedido.productos.add(producto)
    pedido.total += producto.precio
    pedido.save()
    return render(request, 'pedido.html', {'pedidoPerso': pedido})