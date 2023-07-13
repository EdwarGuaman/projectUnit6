from django.urls import path
from .views import ProductListAPIView
from django.views.decorators.csrf import csrf_exempt 

urlpatterns = [
    
    path('productlistapi/', ProductListAPIView.as_view(), name='product-list'),
    ## path('Productos/', csrf_exempt(ListarProductos)),
    ## path('Promociones/',csrf_exempt( ListarPromocion)),
    ## path('Descuentos/', csrf_exempt(ListarDescuento)),

]