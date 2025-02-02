from django.shortcuts import render, redirect
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from admin_resume.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required

from admin_resume.models import Experience, UserProfile

def index(request):
    context = {
        'parent': '',
        'segment': 'index'
    }
    return render(request, 'pages/index.html', context)



class ExperienceView(LoginRequiredMixin, TemplateView):
    template_name = 'experiences/experience.html'
    
    def get(self, request):
        """Affiche la page principale des expériences"""
        experiences = Experience.objects.filter(
            user=request.user.userprofile,
            status='active'
        )
        context = {
            'page_title': 'Expériences professionnelles',
            'page_subtitle': 'Gérez votre parcours professionnel',
            'experiences': experiences
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
            status='active'
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
        
        
def add_experience(self, request):
    """Ajoute une nouvelle expérience"""
    try:
        data = {
            'name': request.POST.get('name'),
            'fonction': request.POST.get('fonction'),
            'entreprise': request.POST.get('entreprise'),
            'date_debut': datetime.strptime(request.POST.get('date_debut'), '%Y-%m-%d'),
            'date_fin': datetime.strptime(request.POST.get('date_fin'), '%Y-%m-%d') if request.POST.get('date_fin') else None,
            'description': request.POST.get('description'),
            'technologies': request.POST.get('technologies'),
            'location': request.POST.get('location'),
            'user': request.user.userprofile,
            'status': 'active'
        }
        
        Experience.objects.create(**data)
        
        return JsonResponse({
            'status': 'success',
            'message': 'Expérience ajoutée avec succès'
        })
        
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

def update_experience(self, request, experience_id):
    """Modifie une expérience existante"""
    try:
        experience = Experience.objects.filter(
            id=experience_id, 
            user=request.user.userprofile,
            status='active'
        )
        
        data = request.POST
        experience.name = data.get('name', experience.name)
        experience.fonction = data.get('fonction', experience.fonction)
        experience.entreprise = data.get('entreprise', experience.entreprise)
        if data.get('date_debut'):
            experience.date_debut = datetime.strptime(data.get('date_debut'), '%Y-%m-%d')
        if data.get('date_fin'):
            experience.date_fin = datetime.strptime(data.get('date_fin'), '%Y-%m-%d')
        experience.description = data.get('description', experience.description)
        experience.technologies = data.get('technologies', experience.technologies)
        experience.location = data.get('location', experience.location)
        
        experience.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Expérience modifiée avec succès'
        })
        
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

def delete_experience(self, request, experience_id):
    """Marque une expérience comme supprimée"""
    try:
        experience = Experience.objects.filter(
            id=experience_id, 
            user=request.user.userprofile,
            status='active'
        )
        experience.status = 'deleted'
        experience.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Expérience supprimée avec succès'
        })
        
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

        

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

def lock_screen(request):
    return render(request, 'pages/auth-lock.html')

# Error and maintenance
def error_404(request):
    return render(request, 'pages/error-404.html')

def error_500(request):
    return render(request, 'pages/error-500.html')

def maintenance(request):
    return render(request, 'pages/error-maintenance.html')


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