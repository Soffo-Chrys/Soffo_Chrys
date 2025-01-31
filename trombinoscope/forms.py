from django import forms
from .models import Etudiant, CV, Competence, Experience, Formation, Langue, Projet

# Formulaire pour le profil d'étudiant
class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'email', 'tel', 'adresse', 'photo']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'placeholder': 'Prénom'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'tel': forms.TextInput(attrs={'placeholder': 'Téléphone'}),
            'adresse': forms.Textarea(attrs={'placeholder': 'Adresse', 'rows': 3}),
        }


from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import re

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import re

class InscriptionForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur'}), required=False)
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer le mot de passe'}))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Votre mot de passe doit contenir au minimum 8 caractères.")
        if password.isdigit():
            raise ValidationError("Votre mot de passe ne peut pas être entièrement numérique.")
        if not re.match(r'^[A-Za-z0-9@.+_-]+$', password):
            raise ValidationError("Le mot de passe ne peut contenir que des lettres, des chiffres et les caractères @, ., +, -, _.")
        return password

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise ValidationError("Les mots de passe ne correspondent pas.")
        return password_confirm

    def save(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        return user

# Formulaire pour les CVs
class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['titre', 'description', 'design']

# Formulaire pour les compétences
class CompetenceForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = ['libelle', 'niveau','cv']

# Formulaire pour les expériences professionnelles
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['poste', 'entreprise', 'date_debut', 'date_fin', 'description','cv']

# Formulaire pour les formations
class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['diplome', 'etablissement', 'date_debut', 'date_fin','cv']

# Formulaire pour les langues
class LangueForm(forms.ModelForm):
    class Meta:
        model = Langue
        fields = ['libelle', 'niveau','cv']

# Formulaire pour les projets
class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['titre', 'description', 'date_debut', 'date_fin','cv']
