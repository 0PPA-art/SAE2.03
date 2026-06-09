# groupes/forms.py
from django import forms
from .models import Groupe  # ← on importe le vrai modèle

class GroupeForm(forms.ModelForm):  # ← ModelForm, pas models.Model
    class Meta:
        model = Groupe
        fields = ['nom']  # adapte selon tes champs