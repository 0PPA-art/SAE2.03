from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from .models import Groupe
from .forms import GroupeForm
from . import models


def ajout(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après unesaisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = GroupeForm(request)
        if form.is_valid(): # validation du formulaire.
            groupes = form.save() # sauvegarde dans la base
            return render(request,"appsabs/affiche.html",{"appsabs" : Livre}) #envoie vers une page d'affichage du bibliothequeapp créé
        else:
            return render(request,"appsabs/ajout_categorie.html",{"form": form})
    else :
        form = GroupeForm() # création d'un formulaire vide
        return render(request,"appsabs/ajout_categorie.html",{"form" : form})

class GroupeListView(ListView):
    model = Groupe
    template_name = 'groupes/liste.html'
    context_object_name = 'groupes'

class GroupeCreateView(CreateView):
    model = Groupe
    form_class = GroupeForm
    template_name = 'groupes/form.html'
    success_url = reverse_lazy('groupe-liste')

class GroupeUpdateView(UpdateView):
    model = models.Groupe.objects.get(pk=id)
    form_class = GroupeForm
    if lform.is_valid():
        Groupe = form_class.save(commit=False)
        Groupe.id = id
        Groupe.save()
        template_name = 'groupes/form.html'
        success_url = reverse_lazy('groupe-liste')
        return HttpResponseRedirect("/bibliothequeapp/")  # plutot que d'avoir un gabarit

class GroupeDeleteView(DeleteView):

    template_name = 'groupes/confirm_delete.html'
    groupe = models.Groupe.objects.get(pk=id)
    livre.delete()
    success_url = reverse_lazy('groupe-liste')
    return HttpResponseRedirect('/bibliothequeapp/liste/')

