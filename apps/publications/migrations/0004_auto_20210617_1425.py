# Generated by Django 3.2.4 on 2021-06-17 14:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_alter_publication_data_create'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='data_create',
        ),
        migrations.AddField(
            model_name='publication',
            name='date_create',
            field=models.DateField(default=datetime.datetime(2021, 6, 17, 14, 25, 56, 767068, tzinfo=utc)),
        ),
    ]