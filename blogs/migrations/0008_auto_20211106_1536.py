# Generated by Django 3.2.7 on 2021-11-06 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20211106_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdata',
            name='img',
        ),
        migrations.AlterField(
            model_name='blogdata',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 6, 15, 36, 34, 135913)),
        ),
    ]
