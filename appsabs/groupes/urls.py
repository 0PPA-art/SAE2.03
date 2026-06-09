from django.urls import path
from .views import *

urlpatterns = [
    path('', liste_groupes, name='groupe-liste'),
    path('ajouter/', ajout_groupe, name='groupe-ajouter'),
    path('modifier/<int:pk>/', modifier_groupe, name='groupe-modifier'),
    path('supprimer/<int:pk>/', supprimer_groupe, name='groupe-supprimer'),
]