# Generated by Django 3.2.4 on 2021-06-19 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_author_prfile_photo'),
        ('publications', '0012_auto_20210619_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='author.author'),
        ),
    ]
