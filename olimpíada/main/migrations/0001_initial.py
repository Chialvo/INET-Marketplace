# Generated by Django 5.1 on 2024-08-26 17:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producto')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='productos',
            field=models.ManyToManyField(through='main.PedidoProducto', to='main.producto'),
        ),
    ]
