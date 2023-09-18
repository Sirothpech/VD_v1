from django.contrib import admin
from .models import ContactMessage  # Assurez-vous d'ajouter l'import du modèle ContactMessage ici

# Enregistrez le modèle ContactMessage dans l'interface d'administration
admin.site.register(ContactMessage)
