from django.shortcuts import render, redirect
from absences.forms import EnseignantForm
from absences.models import Enseignant

def liste_enseignants(request):
    return render(request, 'enseignants/liste.html')

def ajout_enseignant(request):

    if request.method == 'POST':
        form = EnseignantForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/enseignants/')

    else:
        form = EnseignantForm()

    return render(
        request,
        'enseignants/ajout.html',
        {'form': form}
    )
def liste_enseignants(request):
    enseignants = Enseignant.objects.all()

    return render(
        request,
        'enseignants/liste.html',
        {'enseignants': enseignants}
    )