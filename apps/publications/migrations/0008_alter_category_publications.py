# Generated by Django 3.2.4 on 2021-06-19 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0007_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='publications',
            field=models.ManyToManyField(blank=True, to='publications.Publication'),
        ),
    ]