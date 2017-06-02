from django.shortcuts import render
from .models import URL

# Create your views here.
def index(request):
    urls = {}
    for url in URL.objects.all():
        type = url.group.name
        if type not in urls.keys():
            urls[type]=[]
            urls[type].append(url)
        else :urls[type].append(url)
    return render(request, 'index.html', {'urls':urls})