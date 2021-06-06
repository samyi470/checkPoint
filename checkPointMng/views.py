from django.shortcuts import render

from django.http import HttpResponse
from .models import MainMenu


# hello world test
def index(request):
    return render(request,
                  'checkPointMng/home.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


# LAS airport home page
def las(request):
    return render(request,
                  'checkPointMng/las.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


# LAX airport home page
def lax(request):
    return render(request,
                  'checkPointMng/lax.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


# PHX airport home page
def phx(request):
    return render(request,
                  'checkPointMng/phx.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })

