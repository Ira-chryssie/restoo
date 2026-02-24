from django.contrib import admin
from .models import Client, Plat, Commande, LigneCommande

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telephone')
    search_fields = ('nom', 'telephone')


@admin.register(Plat)
class PlatAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')
    search_fields = ('nom',)

class LigneCommandeInline(admin.TabularInline):
    model = LigneCommande
    extra = 1


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id','client', 'date_commande','statut','afficher_total')
    list_filter = ('date_commande','client','statut')
    search_fields = ('client_nom','id')
    inlines = [LigneCommandeInline]

    def afficher_total(self,obj):
        return obj.total_commande()
    afficher_total.short_description = "Total"


@admin.register(LigneCommande)
class LigneCommandeAdmin(admin.ModelAdmin):
    list_display = ('commande', 'plat', 'quantite','sous_total')
    list_filter = ('plat',)
