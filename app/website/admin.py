from django.contrib import admin

# Register your models here.
from .models import Country, Organization #import models

# Register your models here
admin.site.register(Country)
admin.site.register(Organization)