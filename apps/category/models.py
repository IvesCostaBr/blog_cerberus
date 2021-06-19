from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=40)
    photo = models.FileField(upload_to='', blank=True,null=True)
    keyword = models.CharField(max_length=50, default='programming')

    def __str__(self):
        return str(self.title)