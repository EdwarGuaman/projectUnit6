##from django.shortcuts import render
##from django.core.serializers import serialize
##from rest_framework.parsers import JSONParser
##from rest_framework import status
from .models import Categoria, Producto, Promocion, Descuentos
from .serializers import Categoria_Serializers, Producto_Serializers, Promocion_Serializers, Descuentos_Serializers
##from django.http import JsonResponse
##from rest_framework.response import Response
from rest_framework.generics import ListAPIView



# Create your views here.

##def ListarCategoria (request):
##
##  if(request.method=='GET'):
##
##        lista  = Categoria.objects.all()
##        print(lista)
##        ##serializados = Categoria_Serializers(lista, many = True )
##        serializados = serialize('json', lista)
##        print(serializados)
##
##        return JsonResponse(serializados, safe = False )
##
##    if(request.method == 'POST'): ##funcion que me permite ver si se guardo la data envia por POST
##
##        data = JSONParser().parse(request)
##        serializado = Categoria_Serializers(data=data)
##        if(serializado.is_valid()):
##            serializado.save()
##            return JsonResponse(serializado.data, status=status.HTTP_200_OK)
##        
##        return JsonResponse(serializado.errors, status=status.HTTP_400_BAD_REQUEST) ## digame cual es el error y mandame un 400


######################

##def ListarProductos (request):
     
##     if(request.method=='GET'): ##funcion que me permite listar y mostrar la data 
##        lista  = Producto.objects.all()
##        print(lista)
##        serializados = serialize('json', lista)
##        print(serializados)
##    
##        return JsonResponse(serializados, safe = False )
######################

## def ListarPromocion (request):
##     if(request.method=='GET'): ##funcion que me permite listar y mostrar la data 
##        lista  = Promocion.objects.all()
##        print(lista)
##        serializados = serialize('json', lista)
##        print(serializados)
##    
##        return JsonResponse(serializados, safe = False )

######################


#### def ListarDescuento (request):
##     if(request.method=='GET'): ##funcion que me permite listar y mostrar la data 
##        lista  = Descuentos.objects.all()
##        print(lista)
##        serializados = serialize('json', lista)
##        print(serializados)
##    
##        return JsonResponse(serializados, safe = False )

######################
class ProductListAPIView(ListAPIView):
    queryset = Producto.objects.all()
    serializer_class =  Producto_Serializers