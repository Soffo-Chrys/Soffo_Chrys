from django.shortcuts import render
from trombinoscope.models import Etudiant,CV
from django.shortcuts import render
from django.template.loader import render_to_string
from trombinoscope.forms import CVForm
from django.core.paginator import Paginator
# Create your views here.

def trombinoscope(request):
    etudiants = Etudiant.objects.all()
    paginator = Paginator(etudiants, 8)  # 8 étudiants par page
    page_number = request.GET.get('page')
    etudiants = paginator.get_page(page_number)

    utilisateur = request.user if request.user.is_authenticated else None
    return render(request, 'trombinoscope.html', {'etudiants': etudiants, 'utilisateur': utilisateur})



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import InscriptionForm

def inscription(request):
    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()  # Créer l'utilisateur
            login(request, user)  # Connecter automatiquement l'utilisateur
            return redirect('trombinoscope')  # Rediriger vers la page d'accueil (ou trombinoscope)
    else:
        form = InscriptionForm()

    return render(request, 'inscription.html', {'form': form})


def connexion(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('trombinoscope')  # Retour à la page d'accueil
    else:
        form = AuthenticationForm()
    return render(request, 'connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('trombinoscope')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EtudiantForm
from .models import Etudiant

@login_required
def gerer_profil(request):
    # Vérifiez si l'utilisateur a déjà un profil
    etudiant, created = Etudiant.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = EtudiantForm(request.POST, request.FILES, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('trombinoscope')  # Redirection vers la page d'accueil
    else:
        form = EtudiantForm(instance=etudiant)

    return render(request, 'gerer_profil.html', {'form': form})




from django.shortcuts import get_object_or_404

@login_required
def ajouter_cv(request):
    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
            
            # Récupérer l'étudiant lié à l'utilisateur
            etudiant = get_object_or_404(Etudiant, user=request.user)
            cv.etudiant = etudiant  # Associe le CV à l'étudiant

            cv.save()
            return redirect('gestion_cv')  # Exemple de redirection
    else:
        form = CVForm()

    return render(request, 'ajouter_cv.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CompetenceForm

@login_required
def ajouter_competence(request):
    if request.method == 'POST':
        form = CompetenceForm(request.POST)
        if form.is_valid():
            competence = form.save(commit=False)
            competence.utilisateur = request.user  # Associer l'utilisateur connecté
            competence.save()
            return redirect('gestion_cv')  # Rediriger vers l'espace utilisateur
    else:
        form = CompetenceForm()
    
    return render(request, 'ajouter_competence.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def gestion_cv(request):
    return render(request, 'gestion_cv.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ExperienceForm,FormationForm,LangueForm,ProjetForm

@login_required
def ajouter_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience= form.save(commit=False)
            experience.utilisateur = request.user  # Associer l'utilisateur connecté
            experience.save()
            return redirect('gestion_cv')  # Rediriger vers l'espace utilisateur
    else:
        form = ExperienceForm()
    
    return render(request, 'ajouter_experience.html', {'form': form})

@login_required
def ajouter_formation(request):
    if request.method == 'POST':
        form = FormationForm(request.POST)
        if form.is_valid():
            formation= form.save(commit=False)
            formation.utilisateur = request.user  # Associer l'utilisateur connecté
            formation.save()
            return redirect('gestion_cv')  # Rediriger vers l'espace utilisateur
    else:
        form = FormationForm()
    
    return render(request, 'ajouter_formation.html', {'form': form})

@login_required
def ajouter_langue(request):
    if request.method == 'POST':
        form = LangueForm(request.POST)
        if form.is_valid():
            langue= form.save(commit=False)
            langue.utilisateur = request.user  # Associer l'utilisateur connecté
            langue.save()
            return redirect('gestion_cv')  # Rediriger vers l'espace utilisateur
    else:
        form = LangueForm()
    
    return render(request, 'ajouter_langue.html', {'form': form})


@login_required
def ajouter_Projet(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            Projet= form.save(commit=False)
            Projet.utilisateur = request.user  # Associer l'utilisateur connecté
            Projet.save()
            return redirect('gestion_cv')  # Rediriger vers l'espace utilisateur
    else:
        form = ProjetForm()
    
    return render(request, 'ajouter_Projet.html', {'form': form})



def afficher_cv(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)
    etudiant = cv.etudiant
    context = {
        'cv': cv,
        'etudiant': etudiant
    }
    return render(request, 'afficher_cv.html', context)

@login_required
def liste_cvs(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    cvs = CV.objects.filter(etudiant=etudiant)
    context = {
        'etudiant': etudiant,
        'cvs': cvs
    }
    return render(request, 'liste_cvs.html', context)




from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

def telecharger_cv(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)
    html_content = render_to_string('afficher_cv.html', {'cv': cv})
    pdf_file = HTML(string=html_content).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="cv_{cv_id}.pdf"'
    return response



from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from .models import CV
from django.shortcuts import get_object_or_404

def envoyer_cv(request, cv_id):
    # Récupérer l'objet CV
    cv = get_object_or_404(CV, id=cv_id)

    # Rendre le contenu HTML
    html_content = render_to_string('afficher_cv.html', {'cv': cv})
    pdf_file = HTML(string=html_content).write_pdf()

    # Définir l'email
    email = EmailMessage(
        subject=f"Votre CV : {cv.titre}",
        body="Bonjour,\n\nVoici votre CV en pièce jointe.",
        from_email='dutauziet2004@gmail.com',
        to=[request.user.email],  # Utiliser l'email de l'utilisateur connecté
    )

    # Attacher le fichier PDF
    email.attach(f"cv_{cv_id}.pdf", pdf_file, 'application/pdf')

    try:
        # Envoi de l'email
        email.send()
        return HttpResponse("CV envoyé avec succès par e-mail.")
    except Exception as e:
        # En cas d'erreur lors de l'envoi
        return HttpResponse(f"Erreur lors de l'envoi de l'email : {str(e)}")



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CV, Etudiant

@login_required
def lister_modifier_supprimer_cvs(request):
    etudiant = get_object_or_404(Etudiant, user=request.user)
    cvs = CV.objects.filter(etudiant=etudiant)

    if not cvs.exists():
        return render(request, 'lister_modifier_supprimer_cvs.html', {'cvs': cvs, 'message': "Aucun CV trouvé."})

    if request.method == 'POST':
        cv_id = request.POST.get('cv_id')
        cv = CV.objects.filter(id=cv_id, etudiant=etudiant).first()
        if cv:
            cv.delete()
            return redirect('lister_modifier_supprimer_cvs')
        else:
            return render(request, 'lister_modifier_supprimer_cvs.html', {'cvs': cvs, 'error': "CV introuvable."})

    return render(request, 'lister_modifier_supprimer_cvs.html', {'cvs': cvs})

