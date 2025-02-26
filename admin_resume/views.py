from pyexpat.errors import messages
from django.shortcuts import render, redirect
from datetime import datetime
from django.urls import reverse, reverse_lazy
from django.db import transaction
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.db.models import Sum, Q, ExpressionWrapper, F, DurationField
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from admin_resume.enums import ExperienceStatus
from admin_resume.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.decorators import login_required

from admin_resume.models import Experience, UserProfile, Education, EducationStatus

def index(request):
    context = {
        'parent': '',
        'segment': 'index'
    }
    return render(request, 'pages/index.html', context)

# Authentication
class RegistrationView(CreateView):
    template_name = 'pages/sign-up.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class CustomLoginView(LoginView):
    template_name = 'pages/sign-in.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

class LoginViewIllustrator(LoginView):
  template_name = 'pages/sign-in-illustration.html'
  form_class = LoginForm

class LoginViewCover(LoginView):
  template_name = 'pages/sign-in-cover.html'
  form_class = LoginForm

def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')


def login_link(request):
    return render(request, 'pages/sign-in-link.html')

class PasswordReset(PasswordResetView):
  template_name = 'pages/forgot-password.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'pages/password-reset-confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'pages/password-change.html'
  form_class = UserPasswordChangeForm

def terms_service(request):
    return render(request, 'pages/terms-of-service.html')


class ExperienceView(LoginRequiredMixin, TemplateView):
    template_name = 'experiences/experience.html'
    
    def get(self, request):
        """Affiche la page principale des expériences"""
        experiences = Experience.objects.filter(
            Q(status=ExperienceStatus.EN_COURS) | Q(status=ExperienceStatus.TERMINER),
            user=request.user.userprofile
        )
        
        first_experience = experiences.first()

        context = {
            'page_title': 'Expériences professionnelles',
            'page_subtitle': 'Gérez votre parcours professionnel',
            'experiences': experiences,
            'first_experience': first_experience,
            'segment': 'experience'
        }
        return render(request, self.template_name, context)

def experiences_datatables(request):
    """Endpoint pour charger les données des expériences dans DataTables"""
    try:
        items_per_page = 10
        page_number = request.GET.get('page')
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', items_per_page))
        sort_column_index = int(request.GET.get('order[0][column]'))
        sort_direction = request.GET.get('order[0][dir]')
        search = request.GET.get('search[value]', '')
        
        queryset = Experience.objects.filter(
            user=request.user.userprofile,
            status=ExperienceStatus.EN_COURS
        )
        
        # Map column index to corresponding model field for sorting
        sort_columns = {
            1: 'name',
            2: 'fonction',
            3: 'entreprise',
            4: 'date_debut',
            5: 'date_fin',
            6: 'location'
        }
        
        # Apply sorting
        sort_column = sort_columns.get(sort_column_index, 'id')
        if sort_direction == 'desc':
            sort_column = '-' + sort_column
        queryset = queryset.order_by(sort_column)
        
        # Apply search
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(fonction__icontains=search) |
                Q(entreprise__icontains=search) |
                Q(description__icontains=search) |
                Q(location__icontains=search)
            )
        
        paginator = Paginator(queryset, length)
        page_obj = paginator.get_page(page_number)
        
        data = []
        for exp in queryset[start:start + length]:
            data.append({
                'id': exp.id,
                'name': exp.name,
                'fonction': exp.fonction,
                'entreprise': exp.entreprise,
                'date_debut': exp.date_debut.strftime('%Y-%m-%d'),
                'date_fin': exp.date_fin.strftime('%Y-%m-%d') if exp.date_fin else '',
                'description': exp.description,
                'technologies': exp.technologies,
                'location': exp.location,
                'actions': f"""
                    <button class="btn btn-sm btn-primary edit-experience" data-id="{exp.id}">
                        <i class="fas fa-edit"></i> Modifier
                    </button>
                    <button class="btn btn-sm btn-danger delete-experience" data-id="{exp.id}">
                        <i class="fas fa-trash"></i> Supprimer
                    </button>
                """
            })
        
        return JsonResponse({
            'data': data,
            'recordsTotal': queryset.count(),
            'recordsFiltered': paginator.count,
            'draw': int(request.GET.get('draw', 1))
        })
        
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=400)
        
@login_required
@transaction.atomic
def add_experience(request):
    if request.method == 'POST':
        try:
            # Récupération des données du formulaire
            form_data = {
                'name': request.POST.get('name', '').strip(),
                'fonction': request.POST.get('fonction', '').strip(),
                'entreprise': request.POST.get('entreprise', '').strip(),
                'location': request.POST.get('location', '').strip(),
                'technologies': request.POST.get('technologies', '').strip(),
                'description': request.POST.get('description', '').strip(),
                'date_debut': request.POST.get('date_debut'),
                'date_fin': None,
                'en_cours': request.POST.get('en_cours') == 'on',
                'simultaneous_work': request.POST.get('simultaneous_work') == 'true'
            }
            
            # Validation des champs requis
            required_fields = ['name', 'fonction', 'entreprise', 'date_debut', 'description']
            errors = {}
            
            for field in required_fields:
                if not form_data.get(field):
                    errors[field] = _("Ce champ est obligatoire")
            
            if errors:
                return JsonResponse({
                    'status': 0,
                    'message': _("Veuillez corriger les erreurs suivantes"),
                    'errors': errors
                })
            
            # Gestion de la date de fin en fonction de "Poste actuel"
            if not form_data['en_cours'] and request.POST.get('date_fin'):
                form_data['date_fin'] = request.POST.get('date_fin')
            
            # Création de l'expérience avec toutes les données validées
            experience = Experience(
                user=request.user.userprofile,
                name=form_data['name'],
                fonction=form_data['fonction'],
                entreprise=form_data['entreprise'],
                location=form_data['location'],
                technologies=form_data['technologies'],
                description=form_data['description'],
                date_debut=form_data['date_debut'],
                date_fin=form_data['date_fin'],
                status=ExperienceStatus.EN_COURS,
            )
            
            # Ajout de l'attribut pour le travail simultané si nécessaire
            if form_data['simultaneous_work']:
                experience.simultaneous_work = True
                
            experience.save()
            
            return JsonResponse({
                'status': 1,
                'message': _("Expérience ajoutée avec succès !"),
                'redirect': reverse('experience')
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 0,
                'message': str(e)
            }, status=400)
            
@login_required
def edit_experience(request, experience_id):
    """View for fetching experience data to display in edit modal"""
    if request.method == 'GET':
        try:
            # Use filter() instead of get_object_or_404
            experience = Experience.objects.filter(id=experience_id).first()
            if not experience:
                return JsonResponse({'status': 0, 'message': _("Experience not found")})
                
            data = {
                'id': experience.id,
                'entreprise': experience.entreprise,
                'fonction': experience.fonction,
                'date_debut': experience.date_debut.strftime('%Y-%m-%d') if experience.date_debut else None,
                'date_fin': experience.date_fin.strftime('%Y-%m-%d') if experience.date_fin else None,
                'location': experience.location,
                'technologies': experience.technologies,
                'name': experience.name,
                'description': experience.description
            }
            return JsonResponse({'status': 1, 'data': data})
        except Exception as e:
            return JsonResponse({'status': 0, 'message': str(e)})
    return JsonResponse({'status': 0, 'message': _('Method not allowed')})

@transaction.atomic
def update_experience(request, experience_id):
    """View for processing the experience update"""
    if request.method == 'POST':
        try:
            # Use filter() instead of get_object_or_404
            experience = Experience.objects.filter(id=experience_id).first()
            if not experience:
                return JsonResponse({'status': 0, 'message': _("Experience not found")})
            
            # Update experience fields
            experience.entreprise = request.POST.get('entreprise')
            experience.fonction = request.POST.get('fonction')
            experience.date_debut = request.POST.get('date_debut')
            
            # Handle the "current position" checkbox
            if request.POST.get('en_cours') == 'on':
                experience.date_fin = None
            else:
                experience.date_fin = request.POST.get('date_fin')
                
            experience.location = request.POST.get('location')
            experience.technologies = request.POST.get('technologies')
            experience.name = request.POST.get('name')
            experience.description = request.POST.get('description')
            
            # Validate data before saving
            errors = {}
            if not experience.entreprise:
                errors['entreprise'] = _("Ce champ est obligatoire")
            if not experience.fonction:
                errors['fonction'] = _("Ce champ est obligatoire")
            if not experience.date_debut:
                errors['date_debut'] = _("Ce champ est obligatoire")
            if not experience.name:
                errors['name'] = _("Ce champ est obligatoire")
            if not experience.description:
                errors['description'] = _("Ce champ est obligatoire")
                
            if errors:
                return JsonResponse({'status': 0, 'errors': errors})
                
            experience.save()
            return JsonResponse({
                'status': 1,
                'message': _("L'expérience a été mise à jour avec succès")
            })
        except Exception as e:
            return JsonResponse({'status': 0, 'message': str(e)})
    return JsonResponse({'status': 0, 'message': _('Method not allowed')})

@login_required
@transaction.atomic
def delete_experience(request, experience_id):
    # print('@ id de l\'experience:', experience_id)
    if request.method == "POST":
        experience = Experience.objects.get(id=experience_id)
        
        # print('@ details de l\'experience:', experience)

        if not experience:
            return JsonResponse({'statut': 0, 'message': _("Expérience non trouvée.")}, status=404)

        experience.status = ExperienceStatus.SUPPRIMER  # Correction de la virgule
        experience.save()

        return JsonResponse({'statut': 1, 'message': _("Expérience supprimée avec succès !")})
    
    return JsonResponse({'statut': 0, 'message': _("Requête invalide.")}, status=400)

class EducationViews(LoginRequiredMixin, TemplateView):
    template_name = 'education/education.html'
    
    def get(self, request):
        education_list = Education.objects.filter(
            Q(status=EducationStatus.EN_COURS) | Q(status=EducationStatus.TERMINER),
            user=request.user.userprofile).order_by('-date_debut')
        
        status_choices = EducationStatus.choices
        
        context = {
            'education_list': education_list,
            'status_choices': status_choices,
            'segment': 'education',
        }
        return render(request, self.template_name, context)

@login_required
def add_education(request):
    if request.method == 'POST':
        try:
            # Validate required fields
            required_fields = ['nom', 'date_debut', 'intitule', 'etablissement', 'description']
            errors = {}
            
            for field in required_fields:
                if not request.POST.get(field):
                    errors[field] = _("Ce champ est obligatoire")
            
            # Validate date_fin if not en cours
            is_en_cours = request.POST.get('is_en_cours') == 'true'
            
            if not is_en_cours and not request.POST.get('date_fin'):
                errors['date_fin'] = _("La date de fin est obligatoire pour une formation terminée")

            if errors:
                return JsonResponse({
                    'status': 'error',
                    'message': _("Veuillez corriger les erreurs suivantes"),
                    'errors': errors
                })

            # Create education entry
            education = Education.objects.create(
                user=request.user.userprofile,
                nom=request.POST.get('nom'),
                date_debut=request.POST.get('date_debut'),
                date_fin=None if is_en_cours else request.POST.get('date_fin'),
                intitule=request.POST.get('intitule'),
                status=EducationStatus.EN_COURS if is_en_cours else EducationStatus.TERMINER,
                etablissement=request.POST.get('etablissement'),
                description=request.POST.get('description'),
                diplome=request.POST.get('diplome'),
                mention=request.POST.get('mention')
            )
            
            return JsonResponse({
                'status': 'success',
                'message': _('Formation ajoutée avec succès.'),
                'data': {'id': education.id}
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    return JsonResponse({
        'status': 'error',
        'message': _('Méthode non autorisée')
    }, status=405)

@login_required
def update_education(request, education_id):
    if request.method == 'POST':
        try:
            education = Education.objects.filter(
                id=education_id,
                user=request.user.userprofile
            ).first()
            
            if not education:
                return JsonResponse({
                    'status': 'error',
                    'message': _("Formation non trouvée")
                })
            
            required_fields = ['nom', 'date_debut', 'intitule', 'etablissement', 'description']
            errors = {}
            
            for field in required_fields:
                if not request.POST.get(field):
                    errors[field] = _("Ce champ est obligatoire")
            
            is_en_cours = request.POST.get('is_en_cours') == 'true'
            if not is_en_cours and not request.POST.get('date_fin'):
                errors['date_fin'] = _("La date de fin est obligatoire pour une formation terminée")

            if errors:
                return JsonResponse({
                    'status': 'error',
                    'message': _("Veuillez corriger les erreurs suivantes"),
                    'errors': errors
                })
            
            education.nom = request.POST.get('nom')
            education.date_debut = request.POST.get('date_debut')
            education.date_fin = None if is_en_cours else request.POST.get('date_fin')
            education.intitule = request.POST.get('intitule')
            education.status = EducationStatus.EN_COURS if is_en_cours else EducationStatus.TERMINER
            education.etablissement = request.POST.get('etablissement')
            education.description = request.POST.get('description')
            education.diplome = request.POST.get('diplome')
            education.mention = request.POST.get('mention')
            
            education.save()
            
            return JsonResponse({
                'status': 'success',
                'message': _("Formation mise à jour avec succès")
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    return JsonResponse({
        'status': 'error',
        'message': _('Méthode non autorisée')
    }, status=405)


@login_required
def edit_education(request, education_id):
    """View for fetching education data to display in edit modal"""
    if request.method == 'GET':
        try:
            education = Education.objects.filter(
                id=education_id,
                user=request.user.userprofile
            ).first()
            
            if not education:
                return JsonResponse({
                    'status': 'error',
                    'message': _("Formation non trouvée")
                })
            
            # Format dates correctly for date inputs
            date_debut = education.date_debut.strftime('%Y-%m-%d') if education.date_debut else None
            date_fin = education.date_fin.strftime('%Y-%m-%d') if education.date_fin else None
                
            data = {
                'id': education.id,
                'nom': education.nom,
                'date_debut': date_debut,
                'date_fin': date_fin,
                'intitule': education.intitule,
                'status': education.status,
                'etablissement': education.etablissement,
                'description': education.description,
                'diplome': education.diplome or '',
                'mention': education.mention or ''
            }
            
            return JsonResponse({
                'status': 'success',
                'data': data
            })
        except Exception as e:
            return

@login_required
@transaction.atomic
def delete_education(request, education_id):
    if request.method == "POST":
        education = Education.objects.get(id=education_id)
        
        # print('@ details de l\'experience:', experience)

        if not education:
            return JsonResponse({'statut': 0, 'message': _("Education non trouvée.")}, status=404)

        education.status = EducationStatus.SUPPRIMER  # Correction de la virgule
        education.save()

        return JsonResponse({'statut': 1, 'message': _("Education supprimée avec succès !")})
    
    return JsonResponse({'statut': 0, 'message': _("Requête invalide.")}, status=400)




















    

def lock_screen(request):
    return render(request, 'pages/auth-lock.html')

# Error and maintenance
def error_404(request):
    return render(request, 'pages/error-404.html')

def error_500(request):
    return render(request, 'pages/error-500.html')

def maintenance(request):
    return render(request, 'pages/error-maintenance.html')

def page_loader(request):
    context = {
        'parent': 'extra',
        'segment': 'page_loader',
    }
    return render(request, 'pages/page-loader.html', context)


def form_elements(request):
    context = {
        'parent': '',
        'segment': 'form_elements',
    }
    return render(request, 'pages/form-elements.html', context)

def settings(request):
    context = {
        'parent': 'extra',
        'segment': 'settings',
    }
    return render(request, 'pages/settings.html', context)

def changelog(request):
    return render(request, 'pages/changelog.html')

def profile(request):
    return render(request, 'pages/profile.html')

def icons(request):
    context = {
        'parent': '',
        'segment': 'icons',
    }
    return render(request, 'pages/icons.html', context)