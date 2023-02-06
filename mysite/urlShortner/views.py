from django.shortcuts import render
from django.http import HttpResponse
import json

def home(request):
    context = {}
    return render(request,'index.html',context)
