from django.shortcuts import render

from django.http import HttpResponse
from .models import MainMenu

from.models import Throughput


# hello world test
def index(request):
    throughput_list = Throughput.objects.order_by('date')
    labels = []
    data = []
    for throughput in throughput_list:
        labels.append(throughput.date.strftime("%m/%d/%Y"))
        data.append(throughput.throughput)
    return render(request,
                  'checkPointMng/home.html',
                  {
                      'item_list': reversed(list(MainMenu.objects.all())),
                      'labels': labels,
                      'data': data,
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

