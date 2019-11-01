# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile,Neighborhood,Contact,Post,Business
# Register your models here.

admin.site.register(Profile)
admin.site.register(Neighborhood)
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Business)

