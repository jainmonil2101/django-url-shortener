from django.shortcuts import render, redirect
import pyshorteners
from django.contrib.sites.models import Site

current_site = Site.objects.get_current()




def index(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        shortener = pyshorteners.Shortener()
        result = shortener.tinyurl.short(link)
        return render(request, 'index.html', {'result':result, 'domain':current_site.domain})
    else:
        return render(request, 'index.html')
