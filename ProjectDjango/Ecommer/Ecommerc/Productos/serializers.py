from .models import Categoria, Promocion, Descuentos, Producto
from rest_framework import serializers 


class Categoria_Serializers (serializers.ModelSerializer):
    class Meta : 
        model = Categoria
        fields = '__all__'

##################

class Promocion_Serializers (serializers.ModelSerializer):
    class Meta : 
        model = Promocion
        fields = '__all__'
#####################################

class Descuentos_Serializers (serializers.ModelSerializer):
    class Meta : 
        model = Descuentos
        fields = '__all__'

##################

class Producto_Serializers (serializers.ModelSerializer):
    
    idCategoria= Categoria_Serializers(many=False )
    idPromocion= Promocion_Serializers(many=False)
    idDescuentos= Descuentos_Serializers(many=False)

    class Meta : 
        model = Producto
        fields = '__all__'

##################