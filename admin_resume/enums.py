# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

class BaseStatus(models.TextChoices):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    ARCHIVED = 'archived'
    DELETED = 'deleted'

class UserProfileStatus(models.TextChoices):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    BLOCKED = 'blocked'

class ExperienceStatus(models.TextChoices):
    EN_COURS = 'EN COURS'
    TERMINER = 'TERMINER'
    SUPPRIMER = 'SUPPRIMER'

class EducationStatus(models.TextChoices):
    ACTIVE = 'active'
    COMPLETED = 'completed'
    ONGOING = 'ongoing'

class ProfilStatus(models.TextChoices):
    PUBLIC = 'public'
    PRIVATE = 'private'
    HIDDEN = 'hidden'

class ContactStatus(models.TextChoices):
    ACTIVE = 'active'
    ARCHIVED = 'archived'
    PRIVATE = 'private'

class ContactType(models.TextChoices):
    EMAIL = 'email'
    PHONE = 'phone'
    SOCIAL = 'social'
    OTHER = 'other'

class CompetanceStatus(models.TextChoices):
    ACTIVE = 'active'
    ARCHIVED = 'archived'
    LEARNING = 'learning'

class ProjectStatus(models.TextChoices):
    ACTIVE = 'active'
    COMPLETED = 'completed'
    ONGOING = 'ongoing'
    ARCHIVED = 'archived'

class AvisStatus(models.TextChoices):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
ARCHIVED = 'archived'