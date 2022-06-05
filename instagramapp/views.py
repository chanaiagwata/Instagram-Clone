from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Followers, Profile, Post, Comment, Follow
from .forms import DetailsForm, Post, PostForm
# Create your views here.
def main(request):
    '''
    Function that renders the landing page
    '''
    return render(request, 'main.html')

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def showprofile(request):
    posts = Post.objects.all()
    following = Follow.objects.all()
    followers  = Followers.objects.all()
    
    if request.method=='POST':
        details_form = DetailsForm(request.POST, request.Files)
        posts_form = PostForm(request.POST, request.Files)
        
        if details_form.is_valid():
            details_form.save()
            
        if posts_form.is_valid():
            posts_form.save()
            
            return redirect('showprofile')
        else:
            return HttpResponse('Some of the details in your forms are incorrect')
    else:
        return render(request,'showprofile.html', {'details_form':details_form, 'posts_form':posts_form, 'posts':posts, 'following':following, 'followers':followers}) 


# @login_required(login_url='/accounts/login/')