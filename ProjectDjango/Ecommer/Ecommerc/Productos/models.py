from django.db import models

# Create your models here.

class Categoria (models.Model):
    nombre= models.CharField(max_length=30)

    def nombre_Categoria(self):
        return "{}" .format(self.nombre) 
    
    def __str__ (self):
        return self.nombre_Categoria()
####################

class Promocion (models.Model):
    descripcion = models.CharField(max_length=300)
    valor = models.IntegerField()

    def Promocion(self):
        return "{},{}" .format(self.descripcion, self.valor )
    
    def __str__ (self):
        return self.Promocion()
###########################

class Descuentos (models.Model):
    descripcion = models.CharField(max_length=300)
    valor = models.IntegerField()

    def Descuento(self):
        return "{},{}" .format(self.descripcion, self.valor )
    
    def __str__ (self):
        return self.Descuento()


class Producto (models.Model):
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    nombre = models.CharField(max_length=100, default='')
    precio = models.IntegerField()
    cantidadStock = models.IntegerField(verbose_name="Cantidad en Stock")
    descripcion = models.CharField(max_length=300)
    idPromocion = models.ForeignKey(Promocion, on_delete=models.CASCADE, verbose_name="Codigo Promocion", null = True, blank = True)
    idDescuentos = models.ForeignKey(Descuentos, on_delete=models.CASCADE, verbose_name="Codigo Descuento", null = True, blank = True)

#    class Meta:
#         verbose_name='Producto'
#         verbose_name_plural ='Productos'
#         db_table = 'Producto'
#         ordering = 'Producto'

    def Producto(self):
        return "{},{},{},{},{},{}" .format(self.nombre, self.idCategoria, self.precio, self.cantidadStock, self.descripcion, self.idPromocion, self.idDescuentos ) 
    
    def __str__ (self):
        return self.Producto()