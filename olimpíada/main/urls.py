from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .api import *

router = DefaultRouter()
router.register('productos', ProductoViewSet, 'productos')
router.register('pedidos', PedidoViewSet, 'pedidos')
router.register('clientes', ClienteViewSet, 'clientes')

urlpatterns = [
    path('', home, name='home'),
    path('productos/', productos, name='productos'),
    path('login/', login_view, name='login'),  # Ensure this is correct
    path('register/', register, name='register'),
    path('pedido/', pedido, name='pedido'),
    path('pedidos/', pedidos, name='pedidos'),
    path('agregarAlCarrito/<int:id>/', agregarAlCarrito, name='agregarAlCarrito'),
    path('login_cliente/', login_cliente, name='login_cliente'),  # Ensure this is correct
    path('mostrarPedidos/', mostrarPedidos, name='mostrarPedidos')
] + router.urls