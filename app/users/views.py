from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout, hashers
from django.contrib import messages
from .forms import RegisterForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            return redirect("../accounts/login")
    else:
        form = RegisterForm()

    args = {
        "form": form
    }
    return render(request, "forms/register.html", args)
