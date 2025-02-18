from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from admin_resume.models import UserProfile


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            "placeholder": "Password",
            'pattern': r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}',  # Utilisation de chaîne brute (r'...')
            'title': 'Password must contain at least 8 characters, including uppercase, lowercase letters, numbers and special characters'
        }),
    )
    password2 = forms.CharField(
        label=_("Password Confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": "Confirm Password"}),
    )
    
    # Champs supplémentaires du profil
    nom = forms.CharField(
        max_length=255, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Nom"})
    )
    prenoms = forms.CharField(
        max_length=255, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Prénoms"})
    )
    date_naissance = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local',
            "placeholder": "Date de naissance"
        })
    )
    lieu_naissance = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Lieu de naissance"})
    )
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', "placeholder": "Biographie"})
    )
    titre = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Titre"})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'nom', 'prenoms', 'date_naissance', 
                 'lieu_naissance', 'bio', 'titre')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Username",
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                "placeholder": "Email address"
            })
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Création du profil utilisateur
            UserProfile.objects.create(
                user=user,
                nom=self.cleaned_data.get('nom'),
                prenoms=self.cleaned_data.get('prenoms'),
                date_naissance=self.cleaned_data.get('date_naissance'),
                lieu_naissance=self.cleaned_data.get('lieu_naissance'),
                bio=self.cleaned_data.get('bio'),
                titre=self.cleaned_data.get('titre')
            )
        return user
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError(_("Password must be at least 8 characters long."))
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError(_("Password must contain at least one uppercase letter."))
        if not any(char.islower() for char in password1):
            raise forms.ValidationError(_("Password must contain at least one lowercase letter."))
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError(_("Password must contain at least one number."))
        if not any(char in '!@#$%^&*' for char in password1):
            raise forms.ValidationError(_("Password must contain at least one special character (!@#$%^&*)."))
        return password1
    

class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={
            "class": "form-control", 
            "placeholder": "Your username"
        })
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "form-control", 
            "placeholder": "Your password"
        }),
    )

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        "placeholder": "Email address",
    }))

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "New Password",
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "Confirm New Password"
    }), label="Confirm New Password")
    

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "Current Password"
    }), label='Current Password')
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "New Password"
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        "placeholder": "Confirm New Password"
    }), label="Confirm New Password")
