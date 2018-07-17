from django.shortcuts import render
from base_app.models import User, Picture

# Create your views here.


def profile(request, pk=-1):
    cur_id = pk if pk != -1 else get_cur_uid(request)
    user = User.objects.get(uid=cur_id)
    posts = Picture.objects.filter(user=user).order_by('-published_date')
    return render(request, 'user_profile/profile.html', {'user': user, 'posts': posts})


def get_cur_uid(request):
    current_user = request.user
    return current_user.id

