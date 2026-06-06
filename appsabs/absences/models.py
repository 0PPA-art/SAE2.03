from django.db import models
class Groupe(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    def __str__(self):
        return self.prenom + " " + self.nom

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.prenom + " " + self.nom

class Cours(models.Model):
    titre = models.CharField(max_length=100)
    date = models.DateField()
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    duree = models.FloatField()
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    def __str__(self):
        return self.titre

class Absence(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    justifie = models.BooleanField(default=False)
    justification = models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.etudiant) + " absent à " + str(self.cours)
    