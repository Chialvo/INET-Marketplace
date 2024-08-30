from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .serializers import ProductoSerializer, PedidoSerializer
from django.shortcuts import render
from .forms import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test

@login_required(login_url='login')
def home(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return render(request, 'index.html', {'productos': serializer.data})

@login_required(login_url='login')
def productos(request):
    productos = Producto.objects.order_by('codigo')
    serializer = ProductoSerializer(productos, many=True)
    return render(request, 'productos.html', {'productos': serializer.data})

def login_view(request):
    return render(request, "login.html")

@login_required(login_url='login')
def pedido(request):
    productos = Producto.objects.order_by('codigo')
    serializer = ProductoSerializer(productos, many=True)
    return render(request, 'pedido.html', {'productos': serializer.data})

@login_required(login_url='login')
def agregarAlCarrito(request, id):
    producto = Producto.objects.get(pk=id)
    pedido = Pedido.objects.create(cliente=request.user.cliente)
    pedido.productos.add(producto)
    pedido.total += producto.precio
    pedido.save()
    return render(request, 'pedido.html', {'pedidoPerso': pedido})

def login_cliente(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

def mostrarPedidos(request):
    if request.method == 'GET':
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        clientes = Cliente.objects.all() 
        
        context = {
            'pedidos': serializer.data,
            'clientes': clientes,
        }

        return render(request, 'mostrar_pedidos.html', context)

@csrf_exempt
def crear_pedido(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ids = data.get('ids', '').split(',')
        productos = Producto.objects.filter(id__in=ids)
        
        if not productos.exists():
            return JsonResponse({'status': 'error', 'message': 'Productos no encontrados'}, status=400)
        
        pedido = Pedido.objects.create(cliente=request.user)
        
        for producto in productos:
            PedidoProducto.objects.create(pedido=pedido, producto=producto, cantidad=1)  # Ajusta la cantidad según sea necesario
        
        return JsonResponse({'status': 'success', 'message': 'Pedido creado'})
    
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

def register(request):
    if request.method == 'POST':
        form = ClienteRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ClienteRegistrationForm()

    return render(request, 'register.html', {'form': form})

def superuser_required(user):
    return user.is_superuser

@user_passes_test(superuser_required)
def superuser_only_view(request):
    return render(request, 'superuser_only.html')