from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class ClienteManager(BaseUserManager):
    def create_user(self,nombre,direccion,telefono,password):
        if not nombre:
            raise ValueError('El cliente debe tener un nombre')

        cliente = self.model(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono
        )
        cliente.set_password(password)  # Utiliza set_password para encriptar y guardar la contraseña
        cliente.is_active = True
        cliente.save(using=self._db)
        return cliente
    
    def create_superuser(self, nombre, password):
        cliente = self.model(
            nombre=nombre)
        cliente.set_password(password)
        cliente.is_superuser = True
        cliente.is_active = True
        cliente.is_staff = True
        cliente.save(using=self._db)
        return cliente

class Cliente(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'nombre'
    objects = ClienteManager()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descripcion

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Pedido {self.id} de {self.cliente}'

class PedidoProducto(models.Model):
    id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.cantidad}x {self.producto.descripcion}'