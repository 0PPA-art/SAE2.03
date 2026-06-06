from django.shortcuts import render, redirect, get_object_or_404
from absences.forms import CoursForm
from absences.models import Cours


def liste_cours(request):
    cours = Cours.objects.all()
    return render(request, 'cours/liste.html', {'cours': cours})


def ajout_cours(request):
    if request.method == 'POST':
        form = CoursForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/cours/')
    else:
        form = CoursForm()

    return render(request, 'cours/ajout.html', {'form': form})


def modifier_cours(request, id):
    cours = get_object_or_404(Cours, id=id)

    if request.method == 'POST':
        form = CoursForm(request.POST, instance=cours)

        if form.is_valid():
            form.save()
            return redirect('/cours/')
    else:
        form = CoursForm(instance=cours)

    return render(request, 'cours/modifier.html', {'form': form})

def supprimer_cours(request, id):
    cours = get_object_or_404(Cours, id=id)

    if request.method == 'POST':
        cours.delete()
        return redirect('/cours/')

    return render(
        request,
        'cours/supprimer.html',
        {'cours': cours}
    )