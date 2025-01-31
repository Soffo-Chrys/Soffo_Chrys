from django.contrib import admin
from .models import Etudiant, CV, CVDesign, Experience, Formation, Langue, Competence, Projet

# Modèle Etudiant
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'tel', 'adresse', 'photo')
    search_fields = ('nom', 'prenom', 'email')

# Modèle CVDesign
class CVDesignAdmin(admin.ModelAdmin):
    list_display = ('nom', 'template_name')
    search_fields = ('nom',)

# Modèle CV
class CVAdmin(admin.ModelAdmin):
    list_display = ('titre', 'etudiant', 'design')
    search_fields = ('titre', 'etudiant__nom', 'etudiant__prenom')
    list_filter = ('design',)

# Modèle Experience
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('poste', 'entreprise', 'date_debut', 'date_fin', 'cv')
    search_fields = ('poste', 'entreprise')
    list_filter = ('cv',)

# Modèle Formation
class FormationAdmin(admin.ModelAdmin):
    list_display = ('diplome', 'etablissement', 'date_debut', 'date_fin', 'cv')
    search_fields = ('diplome', 'etablissement')
    list_filter = ('cv',)

# Modèle Langue
class LangueAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'niveau', 'cv')
    search_fields = ('libelle',)
    list_filter = ('niveau', 'cv',)

# Modèle Competence
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'niveau', 'cv')
    search_fields = ('libelle',)
    list_filter = ('niveau', 'cv',)

# Modèle Projet
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_debut', 'date_fin', 'cv')
    search_fields = ('titre',)
    list_filter = ('cv',)

# Enregistrement des modèles dans l'admin
admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(CV, CVAdmin)
admin.site.register(CVDesign, CVDesignAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Formation, FormationAdmin)
admin.site.register(Langue, LangueAdmin)
admin.site.register(Competence, CompetenceAdmin)
admin.site.register(Projet, ProjetAdmin)
