from rest_framework import serializers
from .models import Cliente, Producto, Pedido, PedidoProducto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class PedidoProductoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = PedidoProducto
        fields = ['producto', 'cantidad']

class PedidoSerializer(serializers.ModelSerializer):
    productos = PedidoProductoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'