from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .api import *
from django.contrib.auth import views as auth_views

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
    path('agregarAlCarrito/<int:id>/', agregarAlCarrito, name='agregarAlCarrito'),
    path('login_cliente/', login_cliente, name='login_cliente'),  # Ensure this is correct
    path('mostrarPedidos/', mostrarPedidos, name='mostrarPedidos'),
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    path('register/', register, name='register'),    
    path('productos_eliminar/<int:id_producto>/', productos_eliminar, name='delete_producto'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
] + router.urls