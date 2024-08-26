from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def str(self):
        return self.usuario.username

class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def str(self):
        return self.descripcion

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField(Producto, through='PedidoProducto')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def str(self):
        return f'Pedido {self.id} de {self.cliente}'

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def str(self):
        return f'{self.cantidad}x {self.producto.descripcion}'