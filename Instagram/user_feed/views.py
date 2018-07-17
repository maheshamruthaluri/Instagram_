from django.shortcuts import render
from base_app.models import Picture, User
from user_profile.views import get_cur_uid


def feed(request):
    user = User.objects.get(uid=get_cur_uid(request))
    pictures = Picture.objects.all().order_by('published_date')
    return render(request, 'user_feed/feed.html', {'posts': pictures, 'user': user})

