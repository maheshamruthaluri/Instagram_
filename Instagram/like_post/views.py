from django.shortcuts import render
from base_app.models import Picture, Comment, User, Like
from django.core.exceptions import ObjectDoesNotExist
from user_profile.views import get_cur_uid


def like(request, pk):
    user = User.objects.get(uid=get_cur_uid(request))
    picture = Picture.objects.get(pid=pk)
    found = True
    like_obj = None
    try:
        like_obj = Like.objects.get(user=user, picture=picture)
    except ObjectDoesNotExist:
        found = False
    if found:
        picture.likes = picture.likes - 1
        like_obj.delete()
    else:
        like_obj = Like.objects.create(user=user, picture=picture)
        like_obj.save()
        picture.likes = picture.likes + 1
    picture.save()
    comments = Comment.objects.filter(picture=picture).order_by('-published_date')
    return render(request, 'view_post/post.html', {'post': picture, 'comments': comments})

