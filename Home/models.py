from django.db import models
from django.contrib.auth.models import User 
from froala_editor.fields import FroalaField
from .utilities import *
# Create your models here.



class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = FroalaField()
    upload = models.ImageField(upload_to ='blog_images/',max_length=100,blank=True)
    slug = models.SlugField(null=True,blank=True,max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = create_slug(self.title)
        super(Blog, self).save(*args, **kwargs)

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=40,null=True)
    number = models.CharField(max_length=10,null=True)
    desc = models.TextField(null=True)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    token = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.user