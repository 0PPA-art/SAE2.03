from django.shortcuts import render


def liste_etudiants(request):
    return render(request, 'etudiants/liste.html')


def ajout_etudiant(request):
    return render(request, 'etudiants/ajout.html')
