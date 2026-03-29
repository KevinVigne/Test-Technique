from django.db import models

# Create your models here.
class Product(models.Model):
    #Création des propriétés
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()

    #Changement de l'affichage des item  en  (nom - prix € . Date de péremption : date_de_péremption)
    def __str__(self):
        return f"{self.name} - {self.price} € . Date de péremption : {self.expiration_date}"