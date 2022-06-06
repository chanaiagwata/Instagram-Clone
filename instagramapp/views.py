from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Followers, Profile, Post, Comment, Follow
from django.contrib.auth.models import User
from .forms import DetailsForm, PostForm, authform
from django.db.models import F
from .email import send_welcome_email
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

@login_required(login_url='/accounts/login/')
def createpost(request):
    
    createpost = PostForm()
    
    if request.method=='POST':
        form = authform(request.POST)
        if form.is_valid():
            print('valid')
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            user = User(name = name,email = email)
            user.save()
            send_welcome_email(name,email)
            
            
        else:
            form=authform()
            
        createpost = PostForm(request.POST,request.Files)
        if createpost.is_valid():
            createpost.save()
            return redirect('index')
        else:
            return HttpResponse('Your form is incorrect')
    else: render(request, 'createpost_form.html', {'createpost':createpost, 'authform':form})
    
 
@login_required(login_url='/accounts/login/')   
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

@login_required(login_url='/accounts/login/')
def delete_post(request, post_id):
    post_id=int(post_id)
    try:
        post_up=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return redirect('index')
    post_up.delete()
    return redirect('index')

def profile(request):
    posts = Post.objects.all()
    following = Follow.objects.all()
    followers  = Followers.objects.all()
    followercount=len(followers) 
    current_user = request.user 
    
    if request.method=='POST':
        details_form = DetailsForm(request.POST, request.Files)
        posts_form = PostForm(request.POST, request.Files)
        
        if details_form.is_valid():
            profile = details_form.save(commit=False)
            profile.user = current_user
            profile.save()
            
        if posts_form.is_valid():
            post = posts_form.save(commit=False)
            post.profile = current_user.profile
            posts_form.save()
            
        return redirect('profile')
        
    else:
        details_form = DetailsForm
        posts_form = PostForm
        
    return render(request,'profile.html', {'details_form':details_form, 'posts_form':posts_form, 'posts':posts, 'following':following, 'followercount':followercount}) 


# @login_required(login_url='/accounts/login/')