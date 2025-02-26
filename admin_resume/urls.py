from django.urls import path

from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    
    # Experience
    path('experience/', ExperienceView.as_view(), name='experience'),
    path('experiences_datatables/', experiences_datatables, name='experiences_datatables'),
    path('experience/add/', add_experience, name='add_experience'),
    path('experience/edit/<int:experience_id>/', edit_experience, name='edit_experience'),  # New URL for displaying modal
    path('experience/update/<int:experience_id>/', update_experience, name='update_experience'),  # Update action
    path('experience/delete/<int:experience_id>/', delete_experience, name='delete_experience'),
    
    path('education/', EducationViews.as_view(), name='education'),
    path('eductation/add/', add_education, name='add_education'),
    path('eductation/update/<int:education_id>/', update_education, name='update_education'),
    path('eductation/edit/<int:education_id>/', edit_education, name='edit_education'),
    path('eductation/delete/<int:education_id>/', delete_education, name='delete_education'),

    # Authentication
    
    path('accounts/registe/', RegistrationView.as_view(), name='register'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    
    # path('accounts/login/', LoginView.as_view(), name='login'),
    # path('accounts/login-illustration/', LoginViewIllustrator.as_view(), name='login_illustration'),
    # path('accounts/login-cover/', LoginViewCover.as_view(), name='login_cover'),
    path('accounts/logout/', logout_view, name='logout'),
    # path('accounts/login-link/', login_link, name='login_link'),
    # path('accounts/register/', RegistrationView.as_view(), name='register'),
    path('terms-service/', terms_service, name='terms_service'),
    # path('accounts/lock-screen/', lock_screen, name='lock_screen'),

    path('accounts/password-change/', UserPasswordChangeView.as_view(), name='change_password'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='pages/password-change-done.html'
    ), name="password_change_done" ),

    path('accounts/forgot-password/', PasswordReset.as_view(), name='forgot_password'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='pages/password-reset-done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='pages/password-reset-complete.html'
    ), name='password_reset_complete'),

    # Error
    path('error/404/', error_404, name='error_404'),
    path('error/500/', error_500, name='error_500'),
    path('error/maintenance/', maintenance, name='maintenance'),

    path('page-loader/', page_loader, name='page_loader'),

    path('form-elements/', form_elements, name='form_elements'),
    path('settings/', settings, name='settings'),
    
    path('changelog/', changelog, name='changelog'),
    path('profile/', profile, name='profile'),
    path('icons/', icons, name='icons'),
]
