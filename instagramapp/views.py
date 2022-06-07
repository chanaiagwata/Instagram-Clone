from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Followers, Profile, Post, Comment, Follow
from django.contrib.auth.models import User
from .forms import DetailsForm, PostForm, authform
# from django.db.models import F
# from .email import send_welcome_email
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
    form = PostForm()
    posts = Post.objects.all()
    comments = Comment.objects.all()
    return render(request, 'index.html', {'form':form, 'posts':posts, 'comments':comments})

@login_required(login_url='/accounts/login/')
def createpost(request):
    posts = Post.objects.all()
    current_user = request.user
    if request.method=='POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.createpost = current_user.createpost
            post.save()
            
        return redirect('index')
    else:
        form = PostForm
    return render(request, 'createpost_form.html', {'form':form, 'posts':posts})
    
    
 
  
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
    return render(request,'createpost_form.html', {'post_form':post_form})


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
    followingcount=len(following) 
    current_user = request.user 
    
    if request.method=='POST':
        details_form = DetailsForm(request.POST, request.FILES)
        posts_form = PostForm(request.POST, request.FILES)
        
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
        
    return render(request,'profile.html', {'details_form':details_form, 'posts_form':posts_form, 'posts':posts, 'following':following, 'followercount':followercount, 'followingcount':followingcount})

def update_profile(request):
    current_user = request.user
    if request.method== 'POST':
        form = DetailsForm(request.POST, request.FILES)
        if form.is_valid():
            Profile.objects.filter(id=current_user.profile.id).update(bio=form.cleaned_data["bio"])
            profile = Profile.objects.filter(id=current_user.profile.id).first()
            profile.profile_pic.delete()
            profile.profile_pic=form.cleaned_data["profile_pic"]
            profile.save()
        return redirect('profile')
    else:
        form = DetailsForm()
    return render(request, 'update_profile.html', {"form":form})

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


