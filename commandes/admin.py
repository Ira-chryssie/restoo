from django.contrib import admin
from .models import Client, Plat, Commande, LigneCommande


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telephone')


@admin.register(Plat)
class PlatAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('client', 'date_commande')


@admin.register(LigneCommande)
class LigneCommandeAdmin(admin.ModelAdmin):
    list_display = ('commande', 'plat', 'quantite')
