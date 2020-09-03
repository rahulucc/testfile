from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.

def Index(request):
    return render(request,'registration/index.html')

def Login(request):
    
    return render(request,'index.html')

def logout(request):
    return render(request,'/')

 
def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            email= form.save()
            login(request,user)
            return render(request,'registration/index.html')
    context['form']=form
    return render(request,'registration/signup.html',context)
