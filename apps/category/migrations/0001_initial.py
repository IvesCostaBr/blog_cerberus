# Generated by Django 3.2.4 on 2021-06-19 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('photo', models.FileField(blank=True, null=True, upload_to='')),
                ('keyword', models.CharField(default='programming', max_length=50)),
            ],
        ),
    ]
