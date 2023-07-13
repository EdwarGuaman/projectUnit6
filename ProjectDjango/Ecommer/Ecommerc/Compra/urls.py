from django.urls import path
from .views import DetallesConsutasListAPIView
from django.views.decorators.csrf import csrf_exempt 

urlpatterns = [
    path('DetalleConsultalistapi/', DetallesConsutasListAPIView.as_view(), name='profile-list'),

]