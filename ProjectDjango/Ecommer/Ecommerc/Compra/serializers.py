from .models import Carrito, Consulta, DetalleConsulta, Pais, Departamento, Ciudad, Domicilio, FormadePago, Compra, Factura
from rest_framework import serializers 
from django.contrib.auth.models import User


class User_Serializers (serializers.ModelSerializer):
    class Meta : 

        model = User
        fields = '__all__'


class Carrito_Serializers (serializers.ModelSerializer):
    class Meta : 
        model = Carrito
        fields = '__all__'

##################

class Consulta_Serializers (serializers.ModelSerializer):
    class Meta : 
        model = Consulta
        fields = '__all__'

##################

class DetalleConsulta_Serializers (serializers.ModelSerializer):
    
    
    idConsulta = Consulta_Serializers(many=False)
    idUsuario = User_Serializers(many=False)
    
    class Meta : 
        model = DetalleConsulta
        fields = '__all__'

##################

class Pais_Serializers (serializers.ModelSerializer):
    class Meta : 
        model = Pais
        fields = '__all__'

##################

class Departamento_Serializers (serializers.ModelSerializer):
    class Meta : 
        model = Departamento
        fields = '__all__'

##################

class Ciudad_Serializers (serializers.ModelSerializer):
    class Meta : 
        model = Ciudad
        fields = '__all__'

##################

class Domicilio_Serializers (serializers.ModelSerializer):
    class Meta : 
        model = Domicilio
        fields = '__all__'

##################

class FormadePago_Serializers (serializers.ModelSerializer):
    class Meta : 
        model = FormadePago
        fields = '__all__'

##################

class Compra_Serializers (serializers.ModelSerializer):
    class Meta : 
        model = Compra
        fields = '__all__'

##################

class Factura_Serializers (serializers.ModelSerializer):
    class Meta : 
        model = Factura
        fields = '__all__'

##################




