from django.urls import path
from .views import   ProfileListAPIView ##ObtenerPerfiles  ,

urlpatterns = [
     ##path('', ObtenerPerfiles),
     path('profileslistapi/', ProfileListAPIView.as_view(), name='profile-list'),
   ## path("listView/", UserListView.as_view(), name="listView"),
]
