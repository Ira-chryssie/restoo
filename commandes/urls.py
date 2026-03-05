from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from .serializers import MyTokenObtainPairView

router = DefaultRouter()
router.register(r'commandes', views.CommandeViewSet)
router.register(r'plats', views.PlatViewSet)
router.register(r'lignecommandes', views.LigneCommandeViewSet)
router.register(r'clients', views.ClientViewSet)

urlpatterns = [
    path('commandes/', include(router.urls)),
    path('commandes/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('commandes/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('commandes/inscription/', views.inscription, name='inscription'),
    path('api-auth/', include('rest_framework.urls')),
]