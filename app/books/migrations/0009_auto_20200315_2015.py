# Generated by Django 3.0.4 on 2020-03-15 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20200312_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN_Data',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='ISBN_Image',
            field=models.FileField(null=True, upload_to='', verbose_name='ISBN_Image'),
        ),
        migrations.AlterField(
            model_name='book',
            name='current_user',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='deadline_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 23, 15, 9, 384270), null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='detail',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 23, 15, 9, 384365)),
        ),
    ]
