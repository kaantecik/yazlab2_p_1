from django.db import models


class Book(models.Model):

    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    detail = models.CharField(max_length=500, blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    ISBN_Image = models.FileField(
        verbose_name="ISBN_Image", blank=True, null=True)
    ISBN_Data = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
