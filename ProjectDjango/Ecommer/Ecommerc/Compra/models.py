from django.db import models
from Productos.models import Producto, Descuentos
from django.contrib.auth.models import User

# Create your models here.

class Carrito (models.Model):

    cantidad = models.IntegerField()
    idProducto = models.ManyToManyField(Producto, verbose_name="Producto")
   
    def nombre_Carrito(self):
        return "{}, {}" .format(self.cantidad, self.idProducto) 
    
    def __str__ (self):
        return self.nombre_Carrito()

      ###########################    

class Consulta (models.Model):
    descripcion = models.CharField( max_length=300, )
    medico = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Medico")

    class Meta:
        verbose_name='Consulta '
        verbose_name_plural ='Consultas'
        db_table = 'Consulta'
        

    def consulta(self):
        return "{}, {}" .format(self.descripcion, self.medico) 
    
    def __str__ (self):
        return self.consulta()

     ###########################

class DetalleConsulta (models.Model):
    idConsulta =models.ForeignKey(Consulta, on_delete=models.CASCADE, verbose_name="Consulta")
    descripcion = models.CharField( max_length=300)
    idUsuario = models.OneToOneField(User,on_delete=models.CASCADE, verbose_name="Usuario", default='')
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto", default='' )

    def Detalle_Consulta(self):
        return "{}, {}, {}, {}" .format(self.idConsulta, self.idProducto, self.idUsuario, self.descripcion) 
    
    def __str__ (self):
        return self.Detalle_Consulta()
     ###########################

class Pais (models.Model):
    nombre = models.CharField(max_length=70)

    class Meta:
        verbose_name='Pais'
        verbose_name_plural ='Paises'
        db_table = 'Pais'
        

    def nombre_Pais(self):
        return "{}" .format(self.nombre) 
    
    def __str__ (self):
        return self.nombre_Pais()
     
     ###########################

class Departamento (models.Model):
    idPais = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name="Pais")
    nombre = models.CharField(max_length=70)

    class Meta:
        verbose_name='Departamento'
        verbose_name_plural ='Departamentos'
        db_table = 'Departamento'
        

    def nombre_Departamento(self):
        return "{}" .format(self.nombre) 
    
    def __str__ (self):
        return self.nombre_Departamento()
    ###########################

class Ciudad (models.Model):
    idDepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name="Departamento")
    nombre = models.CharField(max_length=30, default='')

    class Meta:
        verbose_name='Ciudad'
        verbose_name_plural ='Ciudades'
        db_table = 'Cuidad'

    def nombre_Ciudad(self):
        return "{}" .format(self.nombre, self.idDepartamento) 
    
    def __str__ (self):
        return self.nombre_Ciudad()
     ###########################

class Domicilio (models.Model):
    direcciondeEntrega = models.CharField(max_length=100)
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario", default='')
    idCiudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad", default='')

    def Domicilio(self):
        return "{}" .format(self.direcciondeEntrega, self.idUsuario, self.idCiudad) 
    
    def __str__ (self):
        return self.Domicilio()

     ###########################

class FormadePago (models.Model):
    opcionesdepago = [
    ("PSE", "PSE"),
    ("TC", "Tarjeta Credito"),
    ("TD", "Tarjeta Debito"),
   
]
    formadepago = models.CharField( choices=opcionesdepago, max_length=10,  verbose_name="Forma de Pago")
    
    def nombre_FormadePago(self):
        return "{}" .format(self.formadepago) 
    
    def __str__ (self):
        return self.nombre_FormadePago()
   ###########################      

class Compra (models.Model):
    Total = models.IntegerField()
    idUsuario = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Usuario")
    idFormadePago = models.ForeignKey(FormadePago, on_delete=models.CASCADE, verbose_name="Forma de Pago" )
    idCarrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, verbose_name="Carrito")
    idDescuento = models.ForeignKey(Descuentos, on_delete=models.CASCADE, verbose_name="Descuento")
    idDetalleConsulta = models.OneToOneField(DetalleConsulta,on_delete=models.CASCADE, verbose_name="Detalle Consulta" )
    idDomicilio = models.OneToOneField(Domicilio, on_delete=models.CASCADE, verbose_name="Domicilio")

    def Compra(self):
        return "{},{},{},{},{},{},{}" .format(self.Total, self.idUsuario, self.idFormadePago, self.idCarrito, self.idDescuento, self.idDetalleConsulta, self.idDomicilio) 
    
    def __str__ (self):
        return self.Compra()

    ########################

class Factura(models.Model):
    idCompra = models.OneToOneField(Compra, on_delete=models.CASCADE, verbose_name="Compra")
    descripcion = models.CharField(max_length=500)

    def nombre_Factura(self):
        return "{},{}" .format(self.idCompra, self.descripcion) 
    
    def __str__ (self):
        return self.nombre_Factura()
     ###########################