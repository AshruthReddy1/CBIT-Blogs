# Generated by Django 3.2.7 on 2021-11-02 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20211101_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdata',
            name='category',
            field=models.CharField(default='General', max_length=30),
        ),
        migrations.AlterField(
            model_name='blogdata',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 20, 48, 51, 785313)),
        ),
    ]
