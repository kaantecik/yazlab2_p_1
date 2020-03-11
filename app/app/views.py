from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from books.models import Book
from books.forms import UploadForm
from django.urls import reverse


def home(request):
    return render(request, "home.html")


@login_required
def books(request):
    books = Book.objects.all()
    args = {"books": books}
    return render(request, "books.html", args)


@login_required
def profile(request):
    books = Book.objects.all()
    args = {"books": books}
    return render(request, "profile.html", args)


@login_required
def upload_book(request):
    form = UploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.author = request.user
        book.name = form.cleaned_data.get("name")
        book.detail = form.cleaned_data.get("detail")
        book.ISBN_Image = form.cleaned_data.get("ISBN_Image")
        book.save()
        return redirect(reverse('profile'))

    args = {"form": form}
    return render(request, "forms/profile_upload_book.html", args)
