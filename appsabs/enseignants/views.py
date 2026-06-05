from django.shortcuts import render


def liste_enseignants(request):
    return render(request, 'enseignants/liste.html')


def ajout_enseignant(request):
    return render(request, 'enseignants/ajout.html')
