from tkinter import CASCADE
from xmlrpc.client import DateTime
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import now
# Create your models here.
class tags(models.Model):
    name = models.CharField(max_length =30)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'postImages', blank=False)
    caption =models.TextField(max_length=500)
    posted_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.author
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    dateTime = models.ForeignKey('self', on_delete=models.CASCADE)
    posted_at = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.user
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)
    bio = models.TextField()
    
    def __str__(self):
        return self.user
    
class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE)
