# Generated by Django 3.2.4 on 2021-06-17 01:27

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='[Sem titulo]', max_length=90)),
                ('bio', models.TextField(max_length=1000)),
                ('data_create', models.DateField(default=datetime.datetime(2021, 6, 17, 1, 27, 55, 298809, tzinfo=utc))),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='author.author')),
            ],
        ),
        migrations.DeleteModel(
            name='Plublication',
        ),
    ]
