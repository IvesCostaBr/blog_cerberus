from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    prfile_photo = models.FileField(upload_to='', blank=True, null=True)

    def __str__(self):
        return str(self.user)