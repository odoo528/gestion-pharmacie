# pharmacie/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('medicaments/', views.liste_medicaments, name='liste_medicaments'),
    path('medicaments/<int:pk>/', views.detail_medicament, name='detail_medicament'),
    path('clients/', views.liste_clients, name='liste_clients'),
    path('commandes/', views.liste_commandes, name='liste_commandes'),
]
