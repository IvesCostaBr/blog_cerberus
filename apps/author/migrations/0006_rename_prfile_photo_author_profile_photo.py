# Generated by Django 3.2.4 on 2021-06-20 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0005_author_localization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='prfile_photo',
            new_name='profile_photo',
        ),
    ]
