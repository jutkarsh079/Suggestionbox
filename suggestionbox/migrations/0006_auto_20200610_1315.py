# Generated by Django 3.0.1 on 2020-06-10 13:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suggestionbox', '0005_auto_20200526_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 10, 13, 15, 40, 791082, tzinfo=utc)),
        ),
    ]
