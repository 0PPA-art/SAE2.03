from django import forms
from .models import Groupe

class GroupeForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields = ['nom', 'annee', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }