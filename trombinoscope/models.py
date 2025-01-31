from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Modèle Etudiant
class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=15)
    adresse = models.TextField()
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"{self.prenom} {self.nom}"


# Modèle Design de CV
class CVDesign(models.Model):
    nom = models.CharField(max_length=50)
    template_name = models.CharField(max_length=100)  # Chemin vers le template HTML

    def str(self):
        return self.nom


# Modèle CV principal
class CV(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    etudiant = models.ForeignKey(Etudiant, related_name="cvs", on_delete=models.CASCADE)
    design = models.ForeignKey(CVDesign, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titre


# Modèle Experience
class Experience(models.Model):
    poste = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    description = models.TextField()
    cv = models.ForeignKey(CV, related_name="experiences", on_delete=models.CASCADE)

    def str(self):
        return f"{self.poste} chez {self.entreprise}"


# Modèle Formation
class Formation(models.Model):
    diplome = models.CharField(max_length=100)
    etablissement = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    cv = models.ForeignKey(CV, related_name="formations", on_delete=models.CASCADE)

    def str(self):
        return f"{self.diplome} - {self.etablissement}"


# Niveaux de compétence/langue
NIVEAU_CHOICES = [
    ('Débutant', 'Débutant'),
    ('Intermédiaire', 'Intermédiaire'),
    ('Avancé', 'Avancé'),
    ('Expert', 'Expert'),
]

## Modèle Langue
class Langue(models.Model):
    libelle = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50, choices=NIVEAU_CHOICES)
    cv = models.ForeignKey(CV, related_name="langues", on_delete=models.CASCADE)

    def str(self):
        return f"{self.libelle} ({self.niveau})"

# Modèle Compétence
class Competence(models.Model):
    libelle = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50, choices=NIVEAU_CHOICES)
    cv = models.ForeignKey(CV, related_name="competences", on_delete=models.CASCADE)

    def str(self):
        return f"{self.libelle} ({self.niveau})"


# Modèle Projet
class Projet(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    cv = models.ForeignKey(CV, related_name="projets", on_delete=models.CASCADE)

    def str(self):
        return self.titre


# Signal pour créer automatiquement un CV si nécessaire
@receiver(post_save, sender=Etudiant)
def create_default_cv(sender, instance, created, **kwargs):
    if created and not instance.cvs.exists():
        CV.objects.create(etudiant=instance, titre="CV par défaut", description="Description par défaut")