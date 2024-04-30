from django.db import models

# Create your models here.

class UsersTIC(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    cognoms = models.CharField(max_length=50)
    assignatures = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)