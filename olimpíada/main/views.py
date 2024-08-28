from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Producto, Pedido
from .serializers import ProductoSerializer, PedidoSerializer

#@login_required(login_url='login')
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

def register(request):
    return render(request, "register.html")

@login_required(login_url='login')
def pedido(request):
    productos = Producto.objects.order_by('codigo')
    serializer = ProductoSerializer(productos, many=True)
    return render(request, 'pedido.html', {'productos': serializer.data})

@login_required(login_url='login') 
def pedidos(request):
    cliente_id = request.GET.get('cliente_id')  # Get the client ID from the request parameters
    pedidos = Pedido.objects.filter(cliente_id=cliente_id)  # Filter the pedidos based on the client ID
    serializer = PedidoSerializer(pedidos, many=True)
    return render(request, 'pedidos.html', {'pedidos': serializer.data})

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
            auth_login(request, user)  # Correctly call the login function
            return redirect('home')  # Redirect to a success page.
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')