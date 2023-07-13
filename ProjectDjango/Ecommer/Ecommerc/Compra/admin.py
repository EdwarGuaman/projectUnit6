from django.contrib import admin
from .models import Carrito, Consulta, DetalleConsulta, Domicilio, Departamento,Pais,Ciudad, FormadePago, Factura, Compra

# Register your models here.
admin.site.register(Carrito)
admin.site.register(Consulta)
admin.site.register(DetalleConsulta)
admin.site.register(Domicilio)
admin.site.register(Pais)
admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(FormadePago)
admin.site.register(Factura)
admin.site.register(Compra)