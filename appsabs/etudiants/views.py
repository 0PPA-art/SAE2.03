# etudiants/views.py
from django.shortcuts import render, redirect, get_object_or_404
from etudiants.forms import EtudiantForm   # ← corrigé
from etudiants.models import Etudiant      # ← corrigé

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiants/liste.html', {'etudiants': etudiants})

def ajout_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/etudiants/')
    else:
        form = EtudiantForm()
    return render(request, 'etudiants/ajout.html', {'form': form})

def modifier_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('/etudiants/')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'etudiants/modifier.html', {'form': form})

def supprimer_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('/etudiants/')
    return render(request, 'etudiants/supprimer.html', {'etudiant': etudiant})


