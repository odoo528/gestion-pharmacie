

from django.shortcuts import render, get_object_or_404
from .models import Medicament, Client, Commande

def liste_medicaments(request):
    medicaments = Medicament.objects.all()
    return render(request, 'pharmacie/liste_medicaments.html', {'medicaments': medicaments})

def detail_medicament(request, pk):
    medicament = get_object_or_404(Medicament, pk=pk)
    return render(request, 'pharmacie/detail_medicament.html', {'medicament': medicament})

def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'pharmacie/liste_clients.html', {'clients': clients})

def liste_commandes(request):
    commandes = Commande.objects.all()
    return render(request, 'pharmacie/liste_commandes.html', {'commandes': commandes})
