# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Neighborhood,Profile,Business,Post,Contact
from django.contrib.auth.decorators import login_required
from .forms import BusinessesForm,PostForm,UpdateProForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    
    place = Neighborhood.objects.all()

    return render(request, 'index.html',{'place':place})


@login_required(login_url='/accounts/login/')
def getProfile(request,users=None):
    user = request.user
    
    
    return render(request,'everything/profile.html')

    
@login_required(login_url='/accounts/login/')
def editProfile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProForm(request.POST,request.FILES)
        if form.is_valid():
            pics = form.save(commit=False)
            pics.user_name = current_user
            pics.save()
        return redirect('profile')

    else:
        form = UpdateProForm()
    return render(request,'everything/profile-edit.html',{"test":form})    