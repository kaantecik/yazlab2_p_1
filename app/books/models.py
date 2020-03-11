from django.db import models


class Book(models.Model):

    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    upload_date = models.DateTimeField(auto_now_add=True)
    ISBN = models.FileField(verbose_name="Image")

    def __str__(self):
        self.name

    class Meta:
        db_table = 'book'
        managed = True
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
