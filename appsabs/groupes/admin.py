from django.contrib import admin
from .models import Groupe

@admin.register(Groupe)
class GroupeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'annee')
    search_fields = ('nom', 'annee')
    list_filter = ('annee',)