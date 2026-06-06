from django.shortcuts import render, redirect, get_object_or_404
from absences.forms import EnseignantForm
from absences.models import Enseignant


def liste_enseignants(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'enseignants/liste.html', {'enseignants': enseignants})


def ajout_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/enseignants/')
    else:
        form = EnseignantForm()

    return render(request, 'enseignants/ajout.html', {'form': form})


def modifier_enseignant(request, id):
    enseignant = get_object_or_404(Enseignant, id=id)

    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)

        if form.is_valid():
            form.save()
            return redirect('/enseignants/')
    else:
        form = EnseignantForm(instance=enseignant)

    return render(request, 'enseignants/modifier.html', {'form': form})

def supprimer_enseignant(request, id):
    enseignant = get_object_or_404(Enseignant, id=id)

    if request.method == 'POST':
        enseignant.delete()
        return redirect('/enseignants/')

    return render(
        request,
        'enseignants/supprimer.html',
        {'enseignant': enseignant}
    )