from django.shortcuts import render
from base_app.models import User
from base_app.forms import LoginForm

# Create your views here.


def login(request):
    user = User()
    form = LoginForm(instance=user)
    return render(request, 'base_app/login.html', {'form': form})

