from django.shortcuts import render

from django.http import HttpResponse
from .models import MainMenu


# hello world test
def index(request):
    return render(request, 'base.html')
