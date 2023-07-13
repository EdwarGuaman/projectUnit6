from .models import Profile, User
from .serializers import Profile_Serializers
## from rest_framework.parsers import JSONParser   ## metodo POST
## from rest_framework import status               ## metodo POST
## from django.views.generic import ListView ,  CreateView, UpdateView, DeleteView

from rest_framework.generics import ListAPIView
##from django.urls import reverse_lazy

# Create your views here.
###################

##def ObtenerPerfiles (request):##

##    if(request.method=='GET'):##
##
##        
##         lista = Profile.objects.select_related().all()
##
##         print(lista)
##         serializados = Profile_Serializers(lista, many = True )
##         ##serializados = serialize('json', lista)
##         print(serializados)
##         ##return JsonResponse(serializados, safe = False )
##         return Response(serializados.data)

    
##class UserListView(ListView):  ##ESTA CLASE ME PERMITE MOSTRAR LA LISTA DEL OBJETO CON UNA PLANTILLA 
##    
##    model = Profile
##    template_name= 'vistauser.html' ### vista a la que apunta en la url 
##    context_object_name = 'object_list'


class ProfileListAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class =  Profile_Serializers