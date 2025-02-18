# Generated by Django 4.1.12 on 2025-02-18 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(blank=True, max_length=255, null=True)),
                ("prenoms", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "date_naissance",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, null=True
                    ),
                ),
                (
                    "lieu_naissance",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("photo", models.TextField(blank=True, max_length=255, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "ACTIVE"),
                            ("inactive", "INACTIVE"),
                            ("blocked", "BLOCKED"),
                        ],
                        default="active",
                        max_length=20,
                    ),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                ("titre", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "UserProfile",
                "verbose_name_plural": "UserProfile",
                "db_table": "user_profil",
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("lien", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "date_debut",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, null=True
                    ),
                ),
                (
                    "date_fin",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, null=True
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "ACTIVE"),
                            ("completed", "COMPLETED"),
                            ("ongoing", "ONGOING"),
                            ("archived", "ARCHIVED"),
                        ],
                        default="active",
                        max_length=20,
                    ),
                ),
                (
                    "technologies",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("client", models.CharField(blank=True, max_length=255, null=True)),
                ("role", models.CharField(blank=True, max_length=255, null=True)),
                ("repository", models.CharField(blank=True, max_length=255, null=True)),
                ("image", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="admin_resume.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Project",
                "verbose_name_plural": "Project",
                "db_table": "project",
            },
        ),
        migrations.CreateModel(
            name="Profil",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("public", "PUBLIC"),
                            ("private", "PRIVATE"),
                            ("hidden", "HIDDEN"),
                        ],
                        default="public",
                        max_length=20,
                    ),
                ),
                ("resume", models.TextField(blank=True, null=True)),
                ("objectifs", models.TextField(blank=True, null=True)),
                ("langues", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "disponibilite",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="admin_resume.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Profil",
                "verbose_name_plural": "Profil",
                "db_table": "profil",
            },
        ),
        migrations.CreateModel(
            name="Loisirs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(blank=True, max_length=255, null=True)),
                ("niveau", models.IntegerField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "ACTIVE"),
                            ("inactive", "INACTIVE"),
                            ("archived", "ARCHIVED"),
                            ("deleted", "DELETED"),
                        ],
                        default="active",
                        max_length=20,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("frequence", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="admin_resume.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Loisirs",
                "verbose_name_plural": "Loisirs",
                "db_table": "loisirs",
            },
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("date_debut", models.DateField()),
                ("date_fin", models.DateField(blank=True, null=True)),
                ("entreprise", models.CharField(max_length=255)),
                ("fonction", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("EN COURS", "En Cours"),
                            ("TERMINER", "Terminer"),
                            ("SUPPRIMER", "Supprimer"),
                        ],
                        default="EN COURS",
                        max_length=20,
                    ),
                ),
                ("description", models.TextField()),
                (
                    "technologies",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("location", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="admin_resume.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Experience",
                "verbose_name_plural": "Experience",
                "db_table": "experience",
                "ordering": ["-date_debut"],
            },
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "annee",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, null=True
                    ),
                ),
                ("intitule", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "ACTIVE"),
                            ("completed", "COMPLETED"),
                            ("ongoing", "ONGOING"),
                        ],
                        default="active",
                        max_length=20,
                    ),
                ),
                (
                    "etablissement",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("diplome", models.CharField(blank=True, max_length=255, null=True)),
                ("mention", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="admin_resume.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Education",
                "verbose_name_plural": "Education",
                "db_table": "education",
            },
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("email", "EMAIL"),
                            ("phone", "PHONE"),
                            ("social", "SOCIAL"),
                            ("other", "OTHER"),
                        ],
                        default="other",
                        max_length=20,
                    ),
                ),
                ("contact", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "ACTIVE"),
                            ("archived", "ARCHIVED"),
                            ("private", "PRIVATE"),
                        ],
                        default="active",
                        max_length=20,
                    ),
                ),
                ("label", models.CharField(blank=True, max_length=255, null=True)),
                ("priorite", models.IntegerField(default=0)),
                ("verified", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="admin_resume.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Contact",
                "verbose_name_plural": "Contact",
                "db_table": "contact",
            },
        ),
        migrations.CreateModel(
            name="Competance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(blank=True, max_length=255, null=True)),
                ("niveau", models.IntegerField(blank=True, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "ACTIVE"),
                            ("archived", "ARCHIVED"),
                            ("learning", "LEARNING"),
                        ],
                        default="active",
                        max_length=20,
                    ),
                ),
                ("categorie", models.CharField(blank=True, max_length=255, null=True)),
                ("certifications", models.TextField(blank=True, null=True)),
                ("annees_experience", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="admin_resume.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Competance",
                "verbose_name_plural": "Competance",
                "db_table": "competance",
            },
        ),
        migrations.CreateModel(
            name="Avis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(blank=True, max_length=255, null=True)),
                ("prenoms", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "date_naissance",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, null=True
                    ),
                ),
                ("ville", models.CharField(blank=True, max_length=255, null=True)),
                ("contact", models.CharField(blank=True, max_length=255, null=True)),
                ("pays", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "PENDING"),
                            ("approved", "APPROVED"),
                            ("rejected", "REJECTED"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("commentaire", models.TextField(blank=True, null=True)),
                ("note", models.IntegerField(default=0)),
                ("relation", models.CharField(blank=True, max_length=255, null=True)),
                ("entreprise", models.CharField(blank=True, max_length=255, null=True)),
                ("poste", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="admin_resume.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Avis",
                "verbose_name_plural": "Avis",
                "db_table": "avis",
            },
        ),
    ]
