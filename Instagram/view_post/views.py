from django.shortcuts import render, get_object_or_404
from base_app.models import Picture, Comment, User
# Create your views here.


def post(request, pk):
    this_post = Picture.objects.get(pid=pk)
    comments = Comment.objects.filter(picture=this_post).order_by('-published_date')
    return render(request, 'view_post/post.html', {'post': this_post, 'comments': comments})

