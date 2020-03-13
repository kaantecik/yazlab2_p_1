from django.forms import ModelForm
from django import forms
from .models import Book


class UploadForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["name", "detail", "ISBN_Image"]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["name", "detail", "ISBN_Image", "is_lent",
                  "current_user", "deadline_date", "upload_date", "ISBN_Data"]
