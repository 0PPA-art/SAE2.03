from django.urls import path

from . import views


urlpatterns = [
    path('', views.liste_cours, name='liste_cours'),
    path('ajout/', views.ajout_cours, name='ajout_cours'),
]
