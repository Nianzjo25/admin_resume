# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .enums import (
    UserProfileStatus, 
    ExperienceStatus, 
    EducationStatus,
    ProfilStatus,
    BaseStatus,
    ContactStatus,
    ContactType,
    CompetanceStatus,
    ProjectStatus,
    AvisStatus
)

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    # id = models.CharField(max_length=255, null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    prenoms = models.CharField(max_length=255, null=True, blank=True)
    date_naissance = models.DateTimeField(blank=True, null=True, default=timezone.now)
    lieu_naissance = models.CharField(max_length=255, null=True, blank=True)
    photo = models.TextField(max_length=255, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name) for status in UserProfileStatus],
        default=UserProfileStatus.ACTIVE.value
    )
    bio = models.TextField(null=True, blank=True)
    titre = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Experience(models.Model):
    #__Experience_FIELDS__
    # id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    date_debut = models.DateTimeField(blank=True, null=True, default=timezone.now)
    date_fin = models.DateTimeField(blank=True, null=True, default=timezone.now)
    entreprise = models.CharField(max_length=255, null=True, blank=True)
    fonction = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.RESTRICT)
    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name) for status in ExperienceStatus],
        default=ExperienceStatus.ACTIVE.value
    )
    description = models.TextField(null=True, blank=True)
    technologies = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #__Experience_FIELDS__END

    class Meta:
        db_table            = _("experience")
        verbose_name        = _("Experience")
        verbose_name_plural = _("Experience")


class Education(models.Model):
    #__Education_FIELDS__
    # id = models.IntegerField(null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    annee = models.DateTimeField(blank=True, null=True, default=timezone.now)
    intitule = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.RESTRICT)
    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name) for status in EducationStatus],
        default=EducationStatus.ACTIVE.value
    )
    etablissement = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    diplome = models.CharField(max_length=255, null=True, blank=True)
    mention = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #__Education_FIELDS__END

    class Meta:
        verbose_name        = _("Education")
        verbose_name_plural = _("Education")


class Profil(models.Model):
    #__Profil_FIELDS__
    # id = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(UserProfile, on_delete=models.RESTRICT)
    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name) for status in ProfilStatus],
        default=ProfilStatus.PUBLIC.value
    )
    resume = models.TextField(null=True, blank=True)
    objectifs = models.TextField(null=True, blank=True)
    langues = models.CharField(max_length=255, null=True, blank=True)
    disponibilite = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #__Profil_FIELDS__END

    class Meta:
        verbose_name        = _("Profil")
        verbose_name_plural = _("Profil")


class Loisirs(models.Model):
    #__Loisirs_FIELDS__
    # id = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    niveau = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.RESTRICT)
    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name) for status in BaseStatus],
        default=BaseStatus.ACTIVE.value
    )
    description = models.TextField(null=True, blank=True)
    frequence = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #__Loisirs_FIELDS__END

    class Meta:
        verbose_name        = _("Loisirs")
        verbose_name_plural = _("Loisirs")


class Contact(models.Model):
    #__Contact_FIELDS__
    # id = models.IntegerField(null=True, blank=True)
    type = models.CharField(
        max_length=20,
        choices=[(type.value, type.name) for type in ContactType],
        default=ContactType.OTHER.value
    )
    contact = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.RESTRICT)
    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name) for status in ContactStatus],
        default=ContactStatus.ACTIVE.value
    )
    label = models.CharField(max_length=255, null=True, blank=True)
    priorite = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #__Contact_FIELDS__END

    class Meta:
        verbose_name        = _("Contact")
        verbose_name_plural = _("Contact")


class Competance(models.Model):
    #__Competance_FIELDS__
    # id = models.IntegerField(null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    niveau = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.RESTRICT)
    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name) for status in CompetanceStatus],
        default=CompetanceStatus.ACTIVE.value
    )
    categorie = models.CharField(max_length=255, null=True, blank=True)
    certifications = models.TextField(null=True, blank=True)
    annees_experience = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #__Competance_FIELDS__END

    class Meta:
        verbose_name        = _("Competance")
        verbose_name_plural = _("Competance")


class Project(models.Model):
    #__Project_FIELDS__
    # id = models.IntegerField(null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    lien = models.CharField(max_length=255, null=True, blank=True)
    date_debut = models.DateTimeField(blank=True, null=True, default=timezone.now)
    date_fin = models.DateTimeField(blank=True, null=True, default=timezone.now)
    user = models.ForeignKey(UserProfile, on_delete=models.RESTRICT)
    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name) for status in ProjectStatus],
        default=ProjectStatus.ACTIVE.value
    )
    technologies = models.CharField(max_length=255, null=True, blank=True)
    client = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    repository = models.CharField(max_length=255, null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #__Project_FIELDS__END

    class Meta:
        verbose_name        = _("Project")
        verbose_name_plural = _("Project")


class Avis(models.Model):
    #__Avis_FIELDS__
    nom = models.CharField(max_length=255, null=True, blank=True)
    prenoms = models.CharField(max_length=255, null=True, blank=True)
    date_naissance = models.DateTimeField(blank=True, null=True, default=timezone.now)
    ville = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    pays = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.RESTRICT)
    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name) for status in AvisStatus],
        default=AvisStatus.PENDING.value
    )
    commentaire = models.TextField(null=True, blank=True)
    note = models.IntegerField(default=0)
    relation = models.CharField(max_length=255, null=True, blank=True)
    entreprise = models.CharField(max_length=255, null=True, blank=True)
    poste = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #__Avis_FIELDS__END

    class Meta:
        verbose_name        = _("Avis")
        verbose_name_plural = _("Avis")



#__MODELS__END