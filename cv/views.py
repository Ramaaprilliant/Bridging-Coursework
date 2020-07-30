from django.shortcuts import render
from django.utils import timezone
from .models import Listing

def cv_list(request):
    posts = Listing.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'cv/cv_list.html', {'cv': posts})
