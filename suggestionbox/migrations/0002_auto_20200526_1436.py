# Generated by Django 3.0.1 on 2020-05-26 14:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suggestionbox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 26, 14, 36, 22, 272636, tzinfo=utc)),
        ),
    ]
