from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _

class Categorie(models.Model):
    nom = models.CharField(_("Nom"), max_length=100)

    def __str__(self):
        return self.nom

class Specialite(models.Model):
    nom = models.CharField(_("Nom"), max_length=100)

    def __str__(self):
        return self.nom

class Instructeur(models.Model):
    nom = models.CharField(_("Nom"), max_length=100)
    prenom = models.CharField(_("Prénom"), max_length=100)
    email = models.EmailField(_("Email"), unique=True)
    specialites = models.ManyToManyField(Specialite, verbose_name=_("Spécialités"))

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Client(models.Model):
    nom = models.CharField(_("Nom"), max_length=100)
    email = models.EmailField(_("Email"), unique=True)

    def __str__(self):
        return self.nom

class Personnel(models.Model):
    nom = models.CharField(_("Nom"), max_length=100)
    prenom = models.CharField(_("Prénom"), max_length=100)
    email = models.EmailField(_("Email"), unique=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Formation(models.Model):
    titre = models.CharField(_("Titre"), max_length=100)
    description = models.TextField(_("Description"))
    prix = models.PositiveBigIntegerField()
    lieu = models.CharField(_("Lieu"), max_length=255)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name=_("Catégorie"))
    instructeur = models.ForeignKey(Instructeur, on_delete=models.CASCADE, verbose_name=_("Instructeur"))
    participants = models.ManyToManyField(Client, through='Inscription', verbose_name=_("Participants"))
    personnel = models.ManyToManyField(Personnel, verbose_name=_("Personnel"))

    def __str__(self):
        return self.titre

class Inscription(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} - {self.formation}"


class Session(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name='sessions')
    date_debut = models.DateField(_("Date de début"))
    date_fin = models.DateField(_("Date de fin"))
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    lieu = models.CharField(_("Lieu"), max_length=255)