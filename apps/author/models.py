from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=30, blank=True, null=True)
    instagram = models.CharField(max_length=60, blank=True, null=True)
    linkedin = models.CharField(max_length=60, blank=True, null=True)
    github = models.CharField(max_length=60, blank=True, null=True)
    curriculo = models.CharField(max_length=60, blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)
    profile_photo = models.FileField(upload_to='', blank=True, null=True)
    localization = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return str(self.user)