from django.shortcuts import render


def liste_cours(request):
    return render(request, 'cours/liste.html')


def ajout_cours(request):
    return render(request, 'cours/ajout.html')
