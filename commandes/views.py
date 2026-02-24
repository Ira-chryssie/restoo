from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client','plats']


class PlatViewSet(viewsets.ModelViewSet):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [ 'prix']
    permission_classes = [IsAuthenticatedOrReadOnly]  

class LigneCommandeViewSet(viewsets.ModelViewSet):
    queryset = LigneCommande.objects.all()
    serializer_class = LigneCommandeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['commande', 'plat']
    permission_classes = [IsAuthenticatedOrReadOnly]  

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['nom']
    filterset_fields = {
        'nom': ['exact', 'icontains'],   
    }
    permission_classes = [IsAuthenticatedOrReadOnly]
