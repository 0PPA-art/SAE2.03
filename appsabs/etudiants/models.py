from django.db import models
from groupes.models import Groupe  # ← Cet import doit être là


class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    groupe = models.ForeignKey(
        Groupe,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"