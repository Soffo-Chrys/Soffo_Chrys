from django.urls import path
from . import views

urlpatterns = [
    path('', views.trombinoscope, name='trombinoscope'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('gerer-profil/', views.gerer_profil, name='gerer_profil'),
    path('ajouter-cv/', views.ajouter_cv, name='ajouter_cv'),
    path('ajouter-competence/', views.ajouter_competence, name='ajouter_competence'),
    path('gestion-cv/', views.gestion_cv, name='gestion_cv'),
    path('ajouter-experience/', views.ajouter_experience, name='ajouter_experience'),
    path('ajouter-formation/', views.ajouter_formation, name='ajouter_formation'),
    path('ajouter-langue/', views.ajouter_langue, name='ajouter_langue'),
    path('ajouter-projet/', views.ajouter_Projet, name='ajouter_projet'),
    path('cv/<int:cv_id>/', views.afficher_cv, name='afficher_cv'),
    path('etudiant/<int:etudiant_id>/cvs/', views.liste_cvs, name='liste_cvs'),
    path('cv/<int:cv_id>/telecharger/', views.telecharger_cv, name='telecharger_cv'),
    path('cv/<int:cv_id>/envoyer/', views.envoyer_cv, name='envoyer_cv'),
    path('modifier-cv/', views.lister_modifier_supprimer_cvs, name='lister_modifier_supprimer_cvs'),

]
