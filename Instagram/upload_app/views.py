from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from base_app.models import User, Picture
from .forms import UploadForm


# Create your views here.
def upload(request, pk):
    user = get_object_or_404(User, uid=pk)

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = user.uid
            obj.save()
            posts = Picture.objects.all().order_by('-published_date')
            return HttpResponseRedirect('../../profile', {'user': user, 'posts': posts})
    else:
        form = UploadForm(instance=user)
    return render(request, 'upload_app/upload.html', {'form': form})

