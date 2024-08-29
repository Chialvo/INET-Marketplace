from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class PedidoProductoForm(ModelForm):
    class Meta:
        model = PedidoProducto
        fields = ['producto','cantidad']