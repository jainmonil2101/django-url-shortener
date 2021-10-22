from django.shortcuts import render, redirect
import pyshorteners
from django.contrib.sites.models import Site

current_site = Site.objects.get_current()
print(current_site.domain)



def index(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        shortener = pyshorteners.Shortener()
        result = shortener.tinyurl.short(link)
        return render(request, 'index.html', {'result':result})
    else:
        return render(request, 'index.html')