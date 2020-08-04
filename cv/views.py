from django.shortcuts import render
from django.utils import timezone
from .models import Listing
from .forms import ListingForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

def cv_list(request):
    cvlists = Listing.objects.all()
    return render(request, 'cv/cv_list.html', {'cvlists': cvlists})

@login_required    
def cv_new(request):
    if request.method == "POST":
        cvform = ListingForm(request.POST)
        if cvform.is_valid():
            post = cvform.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('cv_list')
    else:
        cvform = ListingForm()
    return render(request, 'cv/cv_edit.html', {'form': cvform})

@login_required
def cv_edit(request, pk):
    post = get_object_or_404(Listing, pk=pk)
    if request.method == "POST":
        cvform = ListingForm(request.POST, instance=post)
        if cvform.is_valid():
            post = cvform.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('cv_list')
    else:
        cvform = ListingForm(instance=post)
    return render(request, 'cv/cv_edit.html', {'form': cvform})
