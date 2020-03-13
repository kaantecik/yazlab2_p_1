# Generated by Django 3.0.4 on 2020-03-12 22:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20200312_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='timeDiff',
        ),
        migrations.AlterField(
            model_name='book',
            name='deadline_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 1, 22, 30, 612564), null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 1, 22, 30, 612656)),
        ),
    ]