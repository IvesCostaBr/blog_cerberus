# Generated by Django 3.2.4 on 2021-06-19 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('publications', '0013_alter_comentario_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='publication',
        ),
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category'),
        ),
    ]
