from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .api import *


router = DefaultRouter()
router.register('productos', ProductoViewSet, 'productos')
router.register('pedidos', PedidoViewSet, 'pedidos')

urlpatterns = [
    path("", home, name="home"), 
    path('login/', login, name='login'),
    path('register', register, name='register'),
    path('productos/', productos, name='productos'),
] + router.urls
