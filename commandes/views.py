from django.shortcuts import render, get_object_or_404
from .models import Plat, Client, Commande, LigneCommande
from django.shortcuts import render, redirect
from .forms import CommandeForm, LigneCommandeFormSet
from .models import Commande

def liste_plats(request):
    plats = Plat.objects.all()  # récupère tous les plats
    return render(request, 'plats/liste_plats.html', {'plats': plats})

def detail_plat(request, plat_id):
    plat = get_object_or_404(Plat, id=plat_id)
    return render(request, 'plats/detail_plat.html', {'plat': plat})
def liste_commandes(request):
    commandes = Commande.objects.all()
    return render(request, 'commandes/liste_commandes.html', {'commandes': commandes})
def passer_commande(request):
    if request.method == 'POST':
        form_commande = CommandeForm(request.POST)
        formset_lignes = LigneCommandeFormSet(request.POST)

        if form_commande.is_valid() and formset_lignes.is_valid():
            commande = form_commande.save()  # sauvegarde la commande

            lignes = formset_lignes.save(commit=False)
            for ligne in lignes:
                ligne.commande = commande  # lier la ligne à la commande
                ligne.save()
            return redirect('liste_commandes')  # après validation, redirige vers la liste des commandes
    else:
        form_commande = CommandeForm()
        formset_lignes = LigneCommandeFormSet()

    return render(request, 'commandes/passer_commande.html', {
        'form_commande': form_commande,
        'formset_lignes': formset_lignes
    })
