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
    '''
    Function that renders the index page(timeline)
    '''
    posts = Post.objects.all()
    comments = Comment.objects.all()
    return render(request, 'index.html', {'posts':posts, 'comments':comments})

def createpost(request):
    createpost = PostForm()
    if request.method=='POST':
        createpost = PostForm(request.POST,request.Files)
        if createpost.is_valid():
            createpost.save()
            return redirect('index')
        else:
            return HttpResponse('Your form is incorrect')
    else: render(request, 'createpost_form.html', {'createpost':createpost})
    
    
def update_post(request, post_id):
    post_id=int(post_id)
    try:
        post_up=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return redirect('index')
    post_form=PostForm(request.POST or None,instance=post_up)
    if post_form.is_valid():
        post_form.save()
        return redirect('index')
    return render(request,'createpost_form.html', {'update':post_form})

def delete_post(request, post_id):
    post_id=int(post_id)
    try:
        post_up=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return redirect('index')
    post_up.delete()
    return redirect('index')

def showprofile(request):
    posts = Post.objects.all()
    following = Follow.objects.all()
    followers  = Followers.objects.all()
    followercount=len(followers)  
    
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
        return render(request,'showprofile.html', {'details_form':details_form, 'posts_form':posts_form, 'posts':posts, 'following':following, 'followercount':followercount}) 


# @login_required(login_url='/accounts/login/')