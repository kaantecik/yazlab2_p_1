# Generated by Django 3.0.4 on 2020-03-12 22:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200312_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN_Data',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='deadline_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 1, 13, 1, 391082), null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 1, 13, 1, 391166)),
        ),
    ]
