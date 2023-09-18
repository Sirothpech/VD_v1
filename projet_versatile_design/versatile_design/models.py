from django.db import models
from django.contrib.auth.models import User


class ContactMessage(models.Model):
    nom = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.nom
