from django.db import models
from datetime import datetime, timedelta


class Book(models.Model):

    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    current_user = models.CharField(max_length=50, blank=True, null=True)
    detail = models.CharField(max_length=500, blank=True, null=True)
    deadline_date = models.DateTimeField(
        default=datetime.now() + timedelta(days=7, hours=3), null=True)
    is_lent = models.BooleanField(default=False)
    upload_date = models.DateTimeField(
        default=datetime.now() + timedelta(hours=3))

    ISBN_Image = models.FileField(
        verbose_name="ISBN_Image", blank=True, null=True)
    ISBN_Data = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
