from django.shortcuts import render
from django.utils import timezone
from .models import Listing

def cv_list(request):
    cvlists = Listing.objects.all()
    return render(request, 'cv/cv_list.html', {'cvlists': cvlists})
