from django.db import models
from apps.author.models import Author
from django.utils import timezone


class Publication(models.Model):
    title = models.CharField(max_length=90, default='[Sem titulo]')
    bio = models.TextField(max_length=1000)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL)
    data_create = models.DateField(default=timezone.now())

    def __str__(self):
        return str(self.id) + '   ' + str(self.author.user)


