from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    return render(request, 'main.html')

 

def index(request):
    return render(request, 'index.html')


# @login_required(login_url='/accounts/login/')