from django.urls import path
from . import views

#Ajout des URL autorisées
urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('nouvelle/', views.invoice_create, name='invoice_create'),
    path('<int:id>/', views.invoice_detail, name='invoice_detail'),
    path('<int:id>/supprimer/', views.invoice_delete, name='invoice_delete'),
]