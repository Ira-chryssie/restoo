from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

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

@api_view(['POST'])
@permission_classes([AllowAny])
def inscription(request):
    username = request.data.get('email')
    password = request.data.get('password')
    first_name = request.data.get('prenom', '')
    last_name = request.data.get('nom', '')

    if not username or not password:
        return Response({'erreur': 'Email et mot de passe requis.'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'erreur': 'Cet email est déjà utilisé.'}, status=400)

    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=username
    )
    return Response({'message': 'Compte créé avec succès.'}, status=201)