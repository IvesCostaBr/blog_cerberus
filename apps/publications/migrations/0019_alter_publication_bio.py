# Generated by Django 3.2.4 on 2021-06-21 02:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0018_alter_publication_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
