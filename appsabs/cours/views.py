from django.shortcuts import render, redirect
from absences.forms import CoursForm
from absences.models import Cours

def liste_cours(request):
    return render(request, 'cours/liste.html')

def ajout_cours(request):

    if request.method == 'POST':
        form = CoursForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/cours/')

    else:
        form = CoursForm()

    return render(
        request,
        'cours/ajout.html',
        {'form': form}
    )
def liste_cours(request):
    cours = Cours.objects.all()

    return render(
        request,
        'cours/liste.html',
        {'cours': cours}
    )