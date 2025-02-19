from django.urls import path

from .views import CustomLoginView, ExperienceView, LoginView, LoginViewCover, LoginViewIllustrator, PasswordReset, RegistrationView, UserPasswordChangeView, UserPasswordResetConfirmView, add_experience, changelog, delete_experience, error_404, error_500, experiences_datatables, form_elements, icons, index, lock_screen, login_link, logout_view, maintenance, page_loader, terms_service, profile, settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    
    # Experience
    path('experience/', ExperienceView.as_view(), name='experience'),
    path('experiences_datatables/', experiences_datatables, name='experiences_datatables'),
    path('add_experience/', add_experience, name='add_experience'),
    path('delete_experience/<int:experience_id>/', delete_experience, name='delete_experience'),

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
