from django.db import models
from apps.author.models import Author
import datetime
from apps.category.models import Category



class ComentarioManager(models.Manager):
    def lastComents(self, obj):
        return Comentario.objects.filter(publication=obj).order_by('-id')[:10]


class Publication(models.Model):
    title = models.CharField(max_length=90, default='[Sem titulo]')
    bio = models.TextField(max_length=1000)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    date_create = models.DateField(default=datetime.datetime.today)
    photo = models.FileField(upload_to='', blank=True, null=True)


    def __str__(self):
        return str(self.id) + '   ' + str(self.author)



class Comentario(models.Model):
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    publication = models.ForeignKey(Publication, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    objects = ComentarioManager()
