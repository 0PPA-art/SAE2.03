from django.urls import path
from . import views

urlpatterns = [
    path('', views.absences_all),
    path('absences/', views.absences_all),
    path('absence/ajout/', views.absence_ajout),
    path('absence/traitement/', views.absence_traitement),
    path('absence/affiche/<int:id>/', views.absence_affiche),
    path('absence/update/<int:id>/', views.absence_update),
    path('absence/traitementupdate/<int:id>/', views.absence_traitementupdate),
    path('absence/delete/<int:id>/', views.absence_delete),
    path('import/', views.import_absences),
]