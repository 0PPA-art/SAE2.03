from django.shortcuts import render, redirect, get_object_or_404
from .models import Groupe
from .forms import GroupeForm


# ====================== LISTE ======================
def liste_groupes(request):
    groupes = Groupe.objects.all().order_by('nom')
    return render(request, 'groupes/liste.html', {'groupes': groupes})


# ====================== AJOUT ======================
def ajout_groupe(request):
    if request.method == 'POST':
        form = GroupeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groupe-liste')  # ou '/groupes/'
    else:
        form = GroupeForm()

    return render(request, 'groupes/form.html', {'form': form})


# ====================== MODIFICATION ======================
def modifier_groupe(request, pk):
    groupe = get_object_or_404(Groupe, pk=pk)

    if request.method == 'POST':
        form = GroupeForm(request.POST, instance=groupe)
        if form.is_valid():
            form.save()
            return redirect('groupe-liste')
    else:
        form = GroupeForm(instance=groupe)

    return render(request, 'groupes/form.html', {'form': form})


# ====================== SUPPRESSION ======================
def supprimer_groupe(request, pk):
    groupe = get_object_or_404(Groupe, pk=pk)

    if request.method == 'POST':
        groupe.delete()
        return redirect('groupe-liste')

    return render(request, 'groupes/confirm_delete.html', {'groupe': groupe})