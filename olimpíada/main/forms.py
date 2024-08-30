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
        
class ClienteRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion', 'telefono', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")

        return cleaned_data

    def save(self, commit=True):
        cliente = super().save(commit=False)
        cliente.set_password(self.cleaned_data['password'])
        if commit:
            cliente.save()
        return cliente
