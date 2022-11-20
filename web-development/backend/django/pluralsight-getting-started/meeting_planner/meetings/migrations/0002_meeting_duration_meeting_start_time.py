# Generated by Django 4.1.3 on 2022-11-20 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='duration',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='meeting',
            name='start_time',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
    ]
