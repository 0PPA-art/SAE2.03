from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Groupe
from .forms import GroupeForm

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
    model = Groupe
    form_class = GroupeForm
    template_name = 'groupes/form.html'
    success_url = reverse_lazy('groupe-liste')

class GroupeDeleteView(DeleteView):
    model = Groupe
    template_name = 'groupes/confirm_delete.html'
    success_url = reverse_lazy('groupe-liste')