from django.shortcuts import render

from django.http import HttpResponse
from .models import MainMenu

from .models import TerminalThroughput

# LAXDay attempt
import datetime
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
    start = ''
    startYear = ''
    startMonth = ''
    startDay = ''
    end = ''
    endYear = ''
    endMonth = ''
    endDay = ''

    # if (3. form submitted from .html (POST))
    if request.method == 'POST':
        # set form from POST request
        form = LAXDayForm(request.POST, request.FILES)

        # if valid, save form and return with GET parameter
        if form.is_valid():
            terminal = request.POST.get('terminal')
            start = request.POST.get('start')
            end = request.POST.get('end')

            return HttpResponseRedirect('/lax?submitted=True&terminal=' + terminal + '&start=' + start + '&end=' + end)

    # else (GET) (1. display an empty form to be filled out for the first time),
    else:
        form = LAXDayForm()

        # if (4. submitted is passed as GET parameter, set submitted to true)
        if 'submitted' in request.GET:
            submitted = True
            terminal = request.GET.get('terminal')
            start = request.GET.get('start')
            end = request.GET.get('end')
            startDate = datetime.datetime.strptime(start, '%m/%d/%Y')
            endDate = datetime.datetime.strptime(end, '%m/%d/%Y')

            # # access below to utilize ISO calendar
            # print(startDate.year)
            # print(startDate.month)
            # print(startDate.day)

            startYear = startDate.strftime('%Y')
            startMonth = startDate.strftime('%m')
            startDay = startDate.strftime('%d')
            endYear = endDate.strftime('%Y')
            endMonth = endDate.strftime('%m')
            endDay = endDate.strftime('%d')

    # (2., 5. render .html page)
    return render(request,
                  'checkPointMng/lax.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                      'terminal': terminal,
                      'start': start,
                      'startYear': startYear,
                      'startMonth': startMonth,
                      'startDay': startDay,
                      'end': end,
                      'endYear': endYear,
                      'endMonth': endMonth,
                      'endDay': endDay,
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
