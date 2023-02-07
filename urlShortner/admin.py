from django.contrib import admin
from .models import Links

class ChoiceInline(admin.TabularInline):
    model = Links


admin.site.register(Links)
