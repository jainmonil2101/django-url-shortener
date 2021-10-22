from django.shortcuts import render, redirect
import pyshorteners

def index(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        shortener = pyshorteners.Shortener()
        result = shortener.tinyurl.short(link)
        return render(request, 'index.html', {'result':result})
    else:
        return render(request, 'index.html')
