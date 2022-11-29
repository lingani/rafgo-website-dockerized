"""projet_rafgo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from django.conf.urls import include
from . import views # . is shorthand for the current directory
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('', views.index, name='Index'),
    path('home/', views.index, name='Index'),
    path('blog2/', views.blog, name='Blog'),
    path('blog-details/', views.blog_details, name='Blog Details'),
    path('member-details/', views.member_details, name='Member Details'),
    path('project-details/', views.project_details, name='Project Details'),
    path('404/', views.error404, name='Error404'),   
]
