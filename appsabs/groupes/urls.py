from django.urls import path
from .views import *

urlpatterns = [
    path('', GroupeListView.as_view(), name='groupe-liste'),
    path('ajouter/', GroupeCreateView.as_view(), name='groupe-ajouter'),
    path('modifier/<int:pk>/', GroupeUpdateView.as_view(), name='groupe-modifier'),
    path('supprimer/<int:pk>/', GroupeDeleteView.as_view(), name='groupe-supprimer'),
]