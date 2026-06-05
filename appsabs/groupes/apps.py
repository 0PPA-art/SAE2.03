from django.apps import AppConfig


class GroupesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'groupes'  # doit correspondre au nom du dossier
    verbose_name = "Groupes"
