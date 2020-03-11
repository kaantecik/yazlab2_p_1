from django.contrib import admin
from .models import Book
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "ISBN_Image", "ISBN_Data")
    list_display_links = ["name", "author"]
    search_fields = ["name"]
    list_filter = ["author"]

    class Meta:
        model = Book
