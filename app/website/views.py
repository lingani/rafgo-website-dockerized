from django.shortcuts import render
from .menu import Menu
from .models import Country, Organization #import models
import random

menu_principal = Menu()

orgs = Organization.objects.all()
countries = list(set([org.country for org in orgs]))
countries.sort(key=lambda c: c.name)

def sampled_organizations(orgs):
    countries = list(set([org.country for org in orgs]))
    sampled_countries = countries
    if len(countries)>7:
        sampled_countries = random.sample(countries, k=8)
    sample_orgs = [random.choice(c.organization_set.all()) for c in sampled_countries]
    return(sample_orgs)


# Create your views here.
def index(request):
    context = {
        'page' : "home",
        'menu_principal': menu_principal.get_page_menus("home"),
        'action_menu': {"href":"../home", "name":"Nous Rejoindre"},
        'orgs': orgs,
        'sample_orgs': sampled_organizations(orgs),
        'countries': countries,
        "pays": [('Bénin', 'ben', "sampled"), ('Burkina Faso', 'bfa', "sampled" ), ('Burundi', 'bdi'), ('Cameroun', 'cmr'), ('République centrafricaine', 'rca', "sampled"), ('Comores', 'com'), ('Congo (RC)', 'cog', "sampled"), ('Congo (RDC)', 'rdc'), ("Côte d'lvoire", 'rci'), ('Djibouti', 'dji'), ('Gabon', 'gab'), ('Guinée', 'gin'), ('Guinée équatoriale', 'gnq'), ('Madagascar', 'mdg'), ('Mali', 'mli'), ('Niger', 'ner'), ('Rwanda', 'rwa'), ('Sénégal', 'sen'), ('Seychelles', 'syc'), ('Tchad', 'tcd'), ('Togo', 'tgo')]
    }
    return render(request, 'index.html', context)


def blog(request):
    context = {
        'page' : "blog",
        'menu_principal': menu_principal.get_page_menus("blog"),
        'action_menu': {"href":"../home", "name":"Nous Rejoindre"}
    }
    return render(request, 'blog.html', context)


def blog_details(request):
    context = {
        'page' : "blog-details",
        'menu_principal': menu_principal.get_page_menus("blog-details"),
        'action_menu': {"href":"../home", "name":"Nous Rejoindre"}
    }
    return render(request, 'blog-details.html', context)

def member_details(request):
    context = {
        'page' : "member-details",
        'menu_principal': menu_principal.get_page_menus("member-details"),
        'action_menu': {"href":"../home", "name":"Nous Rejoindre"}
    }
    return render(request, 'member-details.html', context)


def project_details(request):
    context = {
        'page' : "member-details",
        'menu_principal': menu_principal.get_page_menus("project-details"),
        'action_menu': {"href":"../home", "name":"Nous Rejoindre"}
    }
    return render(request, 'project-details.html', context)