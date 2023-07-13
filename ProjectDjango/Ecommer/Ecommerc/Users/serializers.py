from .models import Profile
from rest_framework import serializers 
from django.contrib.auth.models import User

 

class User_Serializers (serializers.ModelSerializer):
    class Meta : 

        model = User
        fields = '__all__'

class Profile_Serializers (serializers.ModelSerializer):
    
    User = User_Serializers(many=False )
    class Meta : 

        model = Profile
        fields = '__all__'