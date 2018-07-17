from django.shortcuts import render, redirect, get_object_or_404
from base_app.models import User
from .forms import UserForm

# Create your views here.


def edit_profile(request, pk):
    profile = get_object_or_404(User, uid=pk)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')
    else:
        form = UserForm(instance=profile)
    return render(request, 'user_editProfile/edit_profile.html', {'form': form})

