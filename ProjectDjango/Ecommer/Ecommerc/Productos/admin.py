from django.contrib import admin
from .models import Categoria, Producto, Promocion, Descuentos

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Promocion)
admin.site.register(Descuentos)
