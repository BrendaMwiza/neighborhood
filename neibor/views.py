# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Image,Profile,Comments,Follower
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import Form,NewImageForm,UpdateProForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    
    place = Neighbourhood.objects.all()

    return render(request, 'index.html'{'place':place})

