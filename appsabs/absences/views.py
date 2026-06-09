import csv
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Absence, Etudiant, Cours
from .forms import AbsenceForm


def absences_all(request):
    absences = Absence.objects.all()
    return render(request, "absences/absences_all.html", {"absences": absences})


def absence_ajout(request):
    form = AbsenceForm()
    return render(request, "absences/absence_ajout.html", {"form": form})


def absence_traitement(request):
    form = AbsenceForm(request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/absences/absences/")

    return render(request, "absences/absence_ajout.html", {"form": form})


def absence_affiche(request, id):
    absence = Absence.objects.get(pk=id)
    return render(request, "absences/absence_affiche.html", {"absence": absence})


def absence_update(request, id):
    absence = Absence.objects.get(pk=id)
    form = AbsenceForm(instance=absence)

    return render(
        request,
        "absences/absence_update.html",
        {
            "form": form,
            "id": id
        }
    )


def absence_traitementupdate(request, id):
    absence = Absence.objects.get(pk=id)

    form = AbsenceForm(
        request.POST,
        instance=absence
    )

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/absences/absences/")

    return render(
        request,
        "absences/absence_update.html",
        {
            "form": form,
            "id": id
        }
    )


def absence_delete(request, id):
    absence = Absence.objects.get(pk=id)
    absence.delete()

    return HttpResponseRedirect("/absences/absences/")


def import_absences(request):

    if request.method == "POST":

        fichier = request.FILES["fichier"]

        contenu = fichier.read()

        try:
            lignes = contenu.decode("utf-8-sig").splitlines()
        except UnicodeDecodeError:
            lignes = contenu.decode("latin-1").splitlines()

        lecteur = csv.reader(lignes)

        next(lecteur)

        for ligne in lecteur:

            email_etudiant = ligne[0]
            id_cours = ligne[1]

            etudiant = Etudiant.objects.get(
                email=email_etudiant
            )

            cours = Cours.objects.get(
                pk=id_cours
            )

            Absence.objects.create(
                etudiant=etudiant,
                cours=cours,
                justifie=False,
                justification=""
            )

        return HttpResponseRedirect("/absences/absences/")

    return render(
        request,
        "absences/import_absences.html"
    )