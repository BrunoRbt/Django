from django.contrib import admin
from .models import Post  # Importe o modelo Post

admin.site.register(Post)  # Registre o modelo Post no Admin
