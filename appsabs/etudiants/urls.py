from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_etudiants, name='liste_etudiants'),
    path('ajout/', views.ajout_etudiant, name='ajout_etudiant'),
    path('modifier/<int:id>/', views.modifier_etudiant, name='modifier_etudiant'),
    path('supprimer/<int:id>/', views.supprimer_etudiant, name='supprimer_etudiant'),
]