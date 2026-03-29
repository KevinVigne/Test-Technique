from django.db import models
from products.models import Product

#Création des données de la Facture
class Invoice(models.Model):
    #Déclaration des Propriétés
    #Propriété number a une longueur de maximum 50 charactère et est Unique
    number = models.CharField(max_length=50,unique=True)
    #Propriété clientName a une longueur de 50 charactère maximum
    client_name= models.CharField(max_length=200)
    #Propriété creationDate Récupère la date de Création et l'ajoute automatiquement
    creation_date=models.DateTimeField(auto_now_add=True)

    #Modification de l'affichage de la Facture
    def __str__(self):
        return f"Facture n° {self.number} -  Client :{self.client_name}"

    #Calcul du sous total de l'objet en question
    def total(self):
        return  sum(item.sub_total() for item in self.invoiceitem_set.all())

    #Calcul de la quantité de l'objet en question
    def item_quantity(self):
        return sum(item.quantity for item in self.invoiceitem_set.all())

#Création des Lignes de la Facture
class InvoiceItem(models.Model):
    #Récupération des données de la Facture avec une clé étrangère que l'on stocke a la propriété invoice
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    #De même pour Product
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    #Déclaration de la propriété quantity qui est un INT avec pour valeur par défaut 1 
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    #Calcul du sous total
    def sub_total(self):
        return self.product.price * self.quantity