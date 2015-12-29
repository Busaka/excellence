from django.contrib import admin

from .models import LocalUniversities, InternationalUniversities

# Register your models here.

admin.site.register(LocalUniversities)
admin.site.register(InternationalUniversities)
