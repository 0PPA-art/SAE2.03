from django import forms
from .models import Etudiant
from groupes.models import Groupe

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'email', 'groupe', 'photo']
