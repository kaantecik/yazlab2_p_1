# Generated by Django 3.0.4 on 2020-03-12 01:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200312_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='timeDiff',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='deadline_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 19, 4, 12, 14, 867308), null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 12, 4, 12, 14, 867533)),
        ),
    ]
