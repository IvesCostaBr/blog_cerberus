# Generated by Django 3.2.4 on 2021-06-19 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0011_publication_comentary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='comentary',
        ),
        migrations.AddField(
            model_name='comentario',
            name='publication',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publications.publication'),
        ),
    ]
