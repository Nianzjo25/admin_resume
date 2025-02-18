"""
URL configuration for my_resume_complete project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.views.i18n import JavaScriptCatalog

# try:
#     from rest_framework.authtoken.views import obtain_auth_token
# except:
#     pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("admin_resume.urls")),
    # path("login/jwt/", view=obtain_auth_token),
    path("jsi18n/", JavaScriptCatalog.as_view(domain='djangojs'), name="javascript-catalog"),
]
