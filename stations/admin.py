from django.contrib import admin
from .models import Station, Zone, Line

# Register your models here. This is so that all our models are acceassable on the django admin site
admin.site.register(Station)
admin.site.register(Zone)
admin.site.register(Line)
