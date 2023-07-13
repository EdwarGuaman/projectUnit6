from .models import Carrito, Consulta, DetalleConsulta, Pais, Departamento, Ciudad, Domicilio, FormadePago, Compra, Factura
from .serializers import Carrito_Serializers, Consulta_Serializers, DetalleConsulta_Serializers, Pais_Serializers, Departamento_Serializers, Ciudad_Serializers, Domicilio_Serializers, FormadePago_Serializers, Compra_Serializers, Factura_Serializers
from rest_framework.generics import ListAPIView

# Create your views here.


class DetallesConsutasListAPIView(ListAPIView):
    queryset = DetalleConsulta.objects.all()
    serializer_class =  DetalleConsulta_Serializers




