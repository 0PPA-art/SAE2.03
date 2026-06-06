from django.urls import path

from . import views


urlpatterns = [
    path('', views.liste_etudiants, name='liste_etudiants'),
    path('ajout/', views.ajout_etudiant, name='ajout_etudiant'),
]
