from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom


class Plat(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.nom}({self.prix}F)"


class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    plats = models.ManyToManyField(Plat, through='LigneCommande')

    STATUT_CHOICES = [
        ('EN_ATTENTE', 'En attente'),
        ('PAYEE', 'Payée'),
        ('LIVREE', 'Livrée'),
    ]
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='EN_ATTENTE'
    )

    def __str__(self):
        return f"Commande {self.id} - {self.client.nom}"
    
    def total_commande(self):
        total = 0
        for ligne in self.lignecommande_set.all():
            total += ligne.plat.prix * ligne.quantite
        return total



class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.plat.nom} x {self.quantite}"
    
    def sous_total(self):
        return self.plat.prix * self.quantite
