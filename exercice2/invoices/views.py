from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Invoice , InvoiceItem
from products.models import Product


# Fonction de la page de toutes les factures
def invoice_list (request):
    #Récupération de toute les factures
    invoices = Invoice.objects.all()
    #Découpage de la page en 8
    paginator = Paginator(invoices , 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #Renvoie la page actuelle au template
    return render(request , 'invoices/invoice_list.html' , {'page_obj': page_obj})

# Fonction de la page de création d'une Facture
def invoice_create(request):
    #Récupération des produits
    products = Product.objects.all()
    if request.method == 'POST':
        #Récupération des données du formulaire
        number = request.POST['number']
        client_name = request.POST['client_name']
        #Création de l'objet facture
        invoice = Invoice.objects.create(number=number , client_name= client_name)
        #Récupération de la liste des id des produits 
        products_ids = request.POST.getlist('product_id')
        #Récupération de la liste des quantités des produits
        quantities = request.POST.getlist('quantity')
        #Association des listes products_ids et quantities 
        for product_id, quantity in zip(products_ids , quantities):
            #Si les valeurs ne sont pas vide
            if product_id and quantity:
                product = get_object_or_404(Product, pk=product_id)
                InvoiceItem.objects.create(invoice=invoice,product=product, quantity=int(quantity))
            #Message de succès d'action
            messages.success(request, f'Facture {number} créée avec succès.')
        #Redirection vers la page de détail de la facture
        return redirect('invoice_detail', id=invoice.pk)
    return render(request,'invoices/invoice_form.html',{'products':products})

def invoice_detail(request,id):
    #Récupération de l'id de la facture
    invoice = get_object_or_404(Invoice, pk=id)
    #Récupération des lignes de la factures
    items = invoice.invoiceitem_set.select_related('product').all()
    #Envoi de la facture au template
    return render(request,'invoices/invoice_detail.html',{'invoice':invoice, 'items' :items})

def invoice_delete(request,id):
    #Récupération de la facture
    invoice = get_object_or_404(Invoice, pk =id )
    #Si la méthode est POST
    if request.method =='POST':
        #Enregistrement du numéro de facture
        number = invoice.number
        #Suppression de la facture
        invoice.delete()
        #Message de succès d'action
        messages.success(request,f'Facture {number} supprimée.')
        #Renvoi vers la liste des factures
        return redirect('invoice_list')
    return render(request, 'invoices/invoice_confirm_delete.html',{'invoice':invoice})