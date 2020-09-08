from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

import requests
import logging

logger = logging.getLogger("eCommWeb")


def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect("home/")
    return render(request, 'registration/login.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.warning(request, "USER_NOT_ACTIVE")
                return render(request, 'registration/login.html', {})
        else:
            messages.warning(request, "WRONG_USER")
            return render(request, 'registration/login.html', {})
    else:
        return render(request, 'registration/login.html', {})

# /home/
@login_required
def home(request):
    logger.info(request.GET)
    return render(request, "home.html",)
