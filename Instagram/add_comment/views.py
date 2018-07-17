from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from base_app.models import Picture, Comment, User
from user_profile.views import get_cur_uid
from .forms import CommentForm
# Create your views here.


def comment(request, pk):
    profile = get_object_or_404(User, uid=get_cur_uid(request))
    picture = get_object_or_404(Picture, pid=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        this_comment = form.save(commit=False)
        this_comment = Comment.objects.create(user=profile, picture=picture, text=form.cleaned_data['text'])
        this_comment.user = profile
        this_comment.save()
        comments = Comment.objects.filter(picture=picture).order_by('-published_date')
        return HttpResponseRedirect('../../post/'+str(pk), {'post': picture, 'comments': comments})
        # return render(request, 'view_post/post.html', {'post': picture, 'comments': comments})
    else:
        form = CommentForm(instance=profile)
        return render(request, 'add_comment/comment.html', {'form': form})

