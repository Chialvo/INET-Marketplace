import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

User = get_user_model()

# Cambia estas credenciales según tus necesidades
nombre = 'admin'
password = 'admin'

if not User.objects.filter(nombre=nombre).exists():
    User.objects.create_superuser(nombre=nombre, password=password)
    print(f'Superuser {nombre} created successfully.')
else:
    print(f'Superuser {nombre} already exists.')