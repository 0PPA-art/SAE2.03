from django.db import models

class Groupe(models.Model):
    nom = models.CharField(max_length=100, unique=True, verbose_name="Nom du groupe")
    annee = models.CharField(max_length=20, verbose_name="Année scolaire", blank=True)
    description = models.TextField(blank=True, verbose_name="Description")

    class Meta:
        verbose_name = "Groupe"
        verbose_name_plural = "Groupes"
        ordering = ['nom']
        app_label = 'groupes' 

    def __str__(self):
        return self.nom
