from django.shortcuts import render
from django.http import *
from .forms import *
from django.contrib.auth.models import User
from base_app import models
from django.contrib import messages
from django.contrib import auth

# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            # cleaned_data is a dictionary to store the values of the model
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            auth_user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            new_user = models.User.objects.create(uid=auth_user.id, name=first_name+" "+last_name, email=email, password=password)
            messages.success(request, 'user registration success')
            return HttpResponseRedirect('/')
    else:
        form = userForm()
    return render(request, 'registration/registration.html', {'form': form})


def login(request):
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['pass']

        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('feed')    # render(request, 'user_feed/feed.html')
            else:
                messages.error(request, 'Username doesn\'t not exist')
        except auth.ObjectDoesNotExist:
            print("Invalid username")
    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
   #return render(request, 'registration/login.html')