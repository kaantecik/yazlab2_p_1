from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


@login_required
def books(request):
    args = {"books": books}
    return render(request, "books.html", args)


@login_required
def profile(request):
    args = {"books": books}
    return render(request, "profile.html", args)


@login_required
class upload_book():
    def get(request):
        pass
