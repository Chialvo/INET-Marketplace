# Generated by Django 5.1 on 2024-08-29 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_cliente_id_alter_pedido_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='productos',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='total',
        ),
    ]
