import datetime

from django.shortcuts import render

from django.http import HttpResponse
from .models import MainMenu

from .models import TerminalThroughput

# LAXDay attempt
from django.http import HttpResponseRedirect
from .forms import LAXDayForm


# hello world test
def index(request):
    throughput_list = TerminalThroughput.objects.order_by('date')
    labels = []
    data = []
    for throughput in throughput_list:
        labels.append(throughput.date.strftime("%m/%d/%Y %H:%M:%S"))
        data.append(throughput.throughput)
    return render(request,
                  'checkPointMng/home.html',
                  {
                      'item_list': list(MainMenu.objects.all()),
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


def lax(request):
    submitted = False
    terminal = ''
    primary = ''
    primaryYear = ''
    primaryMonth = ''
    primaryDay = ''
    compare = []

    # if (3. form submitted from .html (POST))
    if request.method == 'POST':
        # set form from POST request
        form = LAXDayForm(request.POST, request.FILES)

        # if valid, save form and return with GET parameter
        if form.is_valid():
            terminal = request.POST.get('terminal')
            primary = request.POST.get('primary')
            compare = request.POST.getlist('compare')

            # printing years compared
            print('years ticked: ')
            print(compare)

            years = ''
            for year in compare:
                years += '&compare=' + year

            return HttpResponseRedirect('/lax?submitted=True&terminal=' + terminal + '&primary=' + primary + years)

    # else (GET) (1. display an empty form to be filled out for the first time),
    else:
        form = LAXDayForm()

        # if (4. submitted is passed as GET parameter, set submitted to true)
        if 'submitted' in request.GET:
            submitted = True
            terminal = request.GET.get('terminal')
            primary = request.GET.get('primary')
            date = datetime.datetime.strptime(primary, '%Y-%m-%d')
            print(date.year)
            primaryYear = date.strftime('%Y')
            print(date.month)
            primaryMonth = date.strftime('%m')
            print(date.day)
            primaryDay = date.strftime('%d')

            compare = request.GET.getlist('compare')
            print(compare)

            print('printing years selected')
            for year in compare:
                print(year)


    # (2., 5. render .html page)
    return render(request,
                  'checkPointMng/lax.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                      'terminal': terminal,
                      'primary': primary,
                      'year': primaryYear,
                      'month': primaryMonth,
                      'day': primaryDay,
                      'compare': compare,
                  })


# PHX airport home page
def phx(request):
    return render(request,
                  'checkPointMng/phx.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


# data preparation page
def datapreparation(request):
    return render(request,
                  'checkPointMng/datapreparation.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })
