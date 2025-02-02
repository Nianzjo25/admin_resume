# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from enum import Enum

class BaseStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    ARCHIVED = 'archived'
    DELETED = 'deleted'

class UserProfileStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    BLOCKED = 'blocked'

class ExperienceStatus(Enum):
    ACTIVE = 'active'
    ARCHIVED = 'archived'
    DRAFT = 'draft'

class EducationStatus(Enum):
    ACTIVE = 'active'
    COMPLETED = 'completed'
    ONGOING = 'ongoing'

class ProfilStatus(Enum):
    PUBLIC = 'public'
    PRIVATE = 'private'
    HIDDEN = 'hidden'

class ContactStatus(Enum):
    ACTIVE = 'active'
    ARCHIVED = 'archived'
    PRIVATE = 'private'

class ContactType(Enum):
    EMAIL = 'email'
    PHONE = 'phone'
    SOCIAL = 'social'
    OTHER = 'other'

class CompetanceStatus(Enum):
    ACTIVE = 'active'
    ARCHIVED = 'archived'
    LEARNING = 'learning'

class ProjectStatus(Enum):
    ACTIVE = 'active'
    COMPLETED = 'completed'
    ONGOING = 'ongoing'
    ARCHIVED = 'archived'

class AvisStatus(Enum):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
ARCHIVED = 'archived'