# Generated by Django 3.2.4 on 2021-06-19 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_author_prfile_photo'),
        ('publications', '0005_alter_publication_date_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=400)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='author.author')),
            ],
        ),
    ]
