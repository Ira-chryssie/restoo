from django.urls import path
from . import views

urlpatterns = [
    path('plats/', views.liste_plats, name='liste_plats'),
    path('plats/<int:plat_id>/', views.detail_plat, name='detail_plat'),
    path('commandes/', views.liste_commandes, name='liste_commandes'),
    path('commande/nouvelle/', views.passer_commande, name='passer_commande'),
    path('commandes/', views.liste_commandes, name='liste_commandes'),
]