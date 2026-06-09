from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_cours, name='liste_cours'),
    path('ajout/', views.ajout_cours, name='ajout_cours'),
    path('modifier/<int:id>/', views.modifier_cours, name='modifier_cours'),
    path('supprimer/<int:id>/', views.supprimer_cours, name='supprimer_cours'),
]