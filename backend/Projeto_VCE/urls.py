"""Projeto_VCE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('api/', include('accounts.urls')),
    path ('api/', include('exams.urls')),
    path ('api/', include('pacients.urls'))
]

# Site Admin - http://127.0.0.1:8000/admin/
# Registar/Alterar/Apagar/... Exames - http://127.0.0.1:8000/api/exams/
# Registar/Alterar/Apagar/... Pacientes- http://127.0.0.1:8000/api/Pacientes/
# Registar/Alterar/Apagar/... Users - http://127.0.0.1:8000/api/users/
# Login - http://127.0.0.1:8000/api/token/login
# Logout - http://127.0.0.1:8000/api/token/logout