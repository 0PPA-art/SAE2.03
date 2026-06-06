from django.shortcuts import render, redirect
from absences.forms import EtudiantForm
from absences.models import Etudiant

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()

    return render(
        request,
        'etudiants/liste.html',
        {'etudiants': etudiants}
    )

def ajout_etudiant(request):

    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/etudiants/')

    else:
        form = EtudiantForm()

    return render(
        request,
        'etudiants/ajout.html',
        {'form': form}
    )