from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'
    
    def validate(self, attrs):
         data = super().validate(attrs)
         return data

class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plat
        fields = '__all__'

class LigneCommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneCommande
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
        class Meta:
            model = Client
            fields = '__all__'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['is_staff'] = self.user.is_staff
        return data
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer