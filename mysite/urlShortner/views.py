from django.shortcuts import render
from django.http import HttpResponse
from .models import Links
from django.shortcuts import redirect
import json
import random
import string

def home(request):
    context = {}
    if request.method == 'POST':
        result = request.POST['slug']
        if result is None:
            result = ''.join(
                (random.choice(string.ascii_lowercase) for x in range(8)))
        link = Links.objects.create(urls = request.POST['urls'],slug = result)
    return render(request,'index.html',context)


def redir(request,slugs):
    data = Links.objects.get(slug = slugs)
    return redirect('../../' + data.urls)