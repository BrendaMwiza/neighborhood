# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    image = models.ImageField(upload_to='pictures/')
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    number = models.IntegerField(default=0,blank=True) 
    
    def save_neighborhood(self):
        self.save()
      
    def delete_neighborhood(self):
        self.delete()
        
    @classmethod
    def get_by_id(cls,id):
        places = cls.objects.filter(id=id)
        return hoods  
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    boi = models.TextField(max_length=300,null=True)
    location = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/')
    
    
    def save_profile(self):
        self.save() 

    @classmethod
    def get_by_id(cls,id):
        profile = Profile.objects.get(user = id)
        return profile
    
    @classmethod
    def get_by_id(cls,id): 
        profile = Profile.objects.filter(user = id).first()
        return profile
     
        
    def __str__(self):
        return self.name
    
class Business(models.Model):
    owner_business = models.CharField(max_length=300)
    business = models.CharField(max_length=300)
    email = models.EmailField(max_length=200)
    description = models.TextField(max_length=200)
    location = models.ForeignKey(Neighborhood,on_delete=models.CASCADE) 
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    
    def save_business(self):
        self.save()
      
    def delete_business(self):
        self.delete()
        
    @classmethod
    def search_business(cls,search_term):
        busy = cls.objects.filter(business__icontains=busy)
        return busy
    
    
    @classmethod
    def get_business_location(cls,location):
       busy=Business.objects.filter(location__pk=location)

       return busy
   
   
    @classmethod
    def get_business_profile(cls,user):
       business = Business.objects.filter(user__pk=user)
       return business
    
    def __str__(self):
        return self.owner_business
    
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=200) 
    location = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
   
    def save_post(self):
        self.save()
    
    @classmethod
    def get_posts_by_location(cls,location):
        post =Post.objects.filter(location__pk=location)
        print(post)
        return post
    
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=300)
    number = models.IntegerField()
    email = models.EmailField(max_length=200)
    location = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    
    @classmethod
    def get_contact_location(cls,location):
        contact = Contact.objects.filter(location__pk=location)
        return contact
    
    def __str__(self):
        return self.name