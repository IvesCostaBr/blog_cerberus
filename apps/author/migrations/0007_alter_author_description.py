# Generated by Django 3.2.4 on 2021-06-21 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0006_rename_prfile_photo_author_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
