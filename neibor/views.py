# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Neighborhood,Profile,Business,Post,Contact
from django.contrib.auth.decorators import login_required
# from .forms import Form,NewImageForm,UpdateProForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    
    place = Neighborhood.objects.all()

    return render(request, 'index.html',{'place':place})

