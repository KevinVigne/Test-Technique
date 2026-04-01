from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Product

# Fonction d'affichage de la liste des Produits
def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products , 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request , 'products/product_list.html' , {'page_obj' : page_obj})

# Fonction de création d'un produit
def product_create(request):
    if request.method == 'POST':
        #Récupération des Valeurs
        name = request.POST['name']
        price = request.POST['price']
        expiration_date = request.POST['expiration_date']
        #Création de l'objet
        Product.objects.create(name = name, price = price, expiration_date = expiration_date)
        #Message en cas d'action réussie
        messages.success(request,f'Produit « {name} » créé avec succès.' )
        #Renvoi vers la page de liste des produits
        return redirect('product_list')
    return render(request, 'products/product_form.html' , {'title' : 'Nouveau produit'})

# Fonction de modification d'un produit
def product_edit(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.expiration_date = request.POST['expiration_date']
        product.save()
        messages.success(request ,f'Produit « {product.name} »  modifié avec succès.')
        return redirect('product_list')
    return render(request, 'products/product_form.html' , {'title' : 'Modifier le produit' , 'product':product} )

# Fonction Supprimer un produit
def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        name = product.name
        product.delete()
        messages.success(request , f'Produit « {name} » supprimé.')
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product' : product})