from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from books.models import Book
from books.forms import UploadForm, UpdateForm
from users.forms import RegisterForm
from django.urls import reverse
from django.conf import settings
from operator import attrgetter
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.db.models import Q
from django.utils.timesince import timesince
import pytz
import cv2
import zbar
import numpy as np


def home(request):
    return render(request, "home.html")


@login_required
def settingspage(request):
    users = User.objects.all()
    books = Book.objects.all()

    addbook_form = UploadForm(request.POST or None, request.FILES or None)
    adduser_form = RegisterForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if addbook_form.is_valid():
            book = addbook_form.save(commit=False)
            book.author = request.user
            book.name = addbook_form.cleaned_data.get("name")
            book.detail = addbook_form.cleaned_data.get("detail")
            book.ISBN_Image = addbook_form.cleaned_data.get("ISBN_Image")
            book.save()
            return redirect(reverse('books'))
        else:
            addbook_form = UploadForm()
        if adduser_form.is_valid():
            adduser_form.save()
        else:
            adduser_form = RegisterForm()

    args = {"users": users, "books": books,
            "addbook_form": addbook_form, "adduser_form": adduser_form}
    return render(request, "profile_settings.html", args)


@login_required
def deletebook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect(reverse('settings'))


@login_required
def returnbook(request, id):
    tz_Turkey = pytz.timezone('Europe/London')
    book = Book.objects.filter(id=id)
    upload_date = Book.objects.get(id=id).upload_date
    deadline_date = Book.objects.get(id=id).deadline_date
    book.update(is_lent=False)
    book.update(current_user=None)
    book.update(upload_date=datetime.now(tz_Turkey)+timedelta(hours=3))
    book.update(deadline_date=None)

    return redirect(reverse('profile'))


@login_required
def lendbook(request, id):
    tz_Turkey = pytz.timezone('Europe/London')
    book = Book.objects.filter(id=id)
    book.update(is_lent=True)
    book.update(current_user=request.user.username)
    # book.update(upload_date=datetime.now()+timedelta(hours=3))
    book.update(deadline_date=datetime.now(tz_Turkey) +
                timedelta(days=7, hours=3))
    return redirect(reverse('profile'))


@login_required
def deleteuser(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect(reverse('settings'))


@login_required
def books(request):
    books = Book.objects.all()
    count = 0
    query = ""
    for book in books:
        if book.current_user == request.user.username and book.is_lent:
            count += 1
    args = {"books": books, "count": count}

    if request.GET:
        query = request.GET['q']
        args['query'] = str(query)

    book_posts = sorted(get_book_queryset(
        query), key=attrgetter('upload_date'), reverse=True)

    args['book_posts'] = book_posts
    return render(request, "books.html", args)


@login_required
def profile(request):
    books = Book.objects.all()
    count = 0
    searched = ''
    query = ""
    tz_Turkey = pytz.timezone('Europe/London')
    current_time = datetime.now(tz_Turkey)
    is_expired = False
    for book in books:
        if book.current_user == request.user.username and book.is_lent:
            count += 1
            if book.upload_date > book.deadline_date:
                is_expired = True

    args = {"books": books, "count": count,
            "searched": searched, "current_time": current_time, "is_expired": is_expired}

    if request.GET:
        query = request.GET['q']
        args['query'] = str(query)
        print(query)

    book_posts = sorted(get_book_queryset(
        query), key=attrgetter('upload_date'), reverse=True)

    args['book_posts'] = book_posts
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
        image = book.ISBN_Image
        imgstr = str(image)
        img = cv2.imread(settings.MEDIA_ROOT + "//" +
                         imgstr, cv2.IMREAD_GRAYSCALE)
        # whatever function you use to read an image file into a numpy array
        scanner = zbar.Scanner()
        results = scanner.scan(img)
        for result in results:
            print(result.data)
        book.ISBN_Data = str(result.data)
        book.save()
        return redirect(reverse('books'))

    args = {"form": form}
    return render(request, "forms/profile_upload_book.html", args)

    # current_book.update(name=update_form.cleaned_data.get("name"))


@login_required
def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    updatebook_form = UpdateForm(request.POST, instance=book)
    args = {}
    if request.method == "POST":
        updatebook_form = UpdateForm(request.POST, instance=book)
        if updatebook_form.is_valid():
            post = updatebook_form.save(commit=False)
            post.save()
            args = {"updatebook_form": updatebook_form}
            return redirect(reverse('settings'))
        """
            book.update(name=updatebook_form.cleaned_data.get("name"))
            book.update(detail=updatebook_form.cleaned_data.get("detail"))
            book.update(is_lent=updatebook_form.cleaned_data.get("is_lent"))
            book.update(
                current_user=updatebook_form.cleaned_data.get("current_user"))
            book.update(
                deadline_date=updatebook_form.cleaned_data.get("deadline_date"))
            book.update(
                upload_date=updatebook_form.cleaned_data.get("upload_date"))
            book.update(
                ISBN_Data=updatebook_form.cleaned_data.get("ISBN_Data"))
            book.update(
                ISBN_Image=updatebook_form.cleaned_data.get("ISBN_Image"))
            # book.save()
            return redirect(reverse('settings'))
            """
    else:
        form = UpdateForm(instance=book)
        args = {"updatebook_form": updatebook_form}

    return render(request, "forms/update_books.html", args)


def get_book_queryset(query=None):
    queryset = []
    queries = query.split(" ")

    for q in queries:
        books = Book.objects.filter(
            Q(name__icontains=q) |
            Q(ISBN_Data__icontains=q)
        ).distinct()

        for book in books:
            queryset.append(book)

    return list(set(queryset))
