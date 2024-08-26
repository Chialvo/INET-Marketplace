from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .api import *


router = DefaultRouter()
router.register('productos', ProductoViewSet, 'productos')
router.register('pedidos', PedidoViewSet, 'pedidos')

urlpatterns = [
    path('', index, name='index'),
] + router.urls
