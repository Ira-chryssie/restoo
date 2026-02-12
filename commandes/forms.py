from django import forms
from .models import Commande, LigneCommande, Client, Plat

class LigneCommandeForm(forms.ModelForm):
    class Meta:
        model = LigneCommande
        fields = ['plat', 'quantite']

LigneCommandeFormSet = forms.inlineformset_factory(
    Commande,
    LigneCommande,
    form=LigneCommandeForm,
    extra=1,
    can_delete=True
)

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['client']
