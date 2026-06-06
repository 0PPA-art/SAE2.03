from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_enseignants, name='liste_enseignants'),
    path('ajout/', views.ajout_enseignant, name='ajout_enseignant'),
    path('modifier/<int:id>/', views.modifier_enseignant, name='modifier_enseignant'),
    path('supprimer/<int:id>/', views.supprimer_enseignant, name='supprimer_enseignant'),
]