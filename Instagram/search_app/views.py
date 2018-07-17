from django.shortcuts import render
from base_app.models import User
from .forms import SearchForm

# Create your views here.


def search_handler(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            user = User.objects.filter(name__icontains=search)
            print(user)
            if user.exists():
                return render(request, 'search_app/search_results.html', {'user': user})
            else:
                return render(request, 'search_app/search_none.html')
    else:
        form = SearchForm()
    return render(request, 'search_app/search.html', {'form': form})