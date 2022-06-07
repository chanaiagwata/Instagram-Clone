from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'images/', blank=True)
    bio = models.TextField()
    
    def __str__(self):
        return self.user
    
    def search_by_username(cls,search_term):
        profile = cls.objects.filter(username__icontains=search_term)
        return profile
    
    
class Post(models.Model):
    pic = models.ImageField(upload_to = 'posts/', blank=False)
    caption =models.TextField(max_length=500)
    posted_at = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.IntegerField(blank=True)

    def __str__(self):
        return {self.profile.user}
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user
    

    
class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.following

class Followers(models.Model):
    followers = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.followers

