from django.urls import path

from . import views


urlpatterns = [
    path('', views.liste_enseignants, name='liste_enseignants'),
    path('ajout/', views.ajout_enseignant, name='ajout_enseignant'),
]
