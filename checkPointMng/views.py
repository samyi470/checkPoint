from django.shortcuts import render

from django.http import HttpResponse
from .models import MainMenu

from .models import TerminalThroughput

import datetime
from django.http import HttpResponseRedirect
from .forms import LAXDayForm
from .forms import LASDayForm
from .forms import PHXDayForm

from statsmodels.tsa.stattools import adfuller
from numpy import log
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
import os


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
        form = LASDayForm(request.POST, request.FILES)

        # if valid, save form and return with GET parameter
        if form.is_valid():
            terminal = request.POST.get('terminal')
            start = request.POST.get('start')
            end = request.POST.get('end')

            return HttpResponseRedirect('/las?submitted=True&terminal=' + terminal + '&start=' + start + '&end=' + end)

    # else (GET) (1. display an empty form to be filled out for the first time),
    else:
        form = LASDayForm()

        # if (4. submitted is passed as GET parameter, set submitted to true)
        if 'submitted' in request.GET:
            submitted = True
            terminal = request.GET.get('terminal')
            start = request.GET.get('start')
            end = request.GET.get('end')
            startDate = datetime.datetime.strptime(start, '%m/%d/%Y')
            endDate = datetime.datetime.strptime(end, '%m/%d/%Y')

            # to utilize ISO calendar - startDate.year/month/day

            startYear = startDate.strftime('%Y')
            startMonth = startDate.strftime('%m')
            startDay = startDate.strftime('%d')
            endYear = endDate.strftime('%Y')
            endMonth = endDate.strftime('%m')
            endDay = endDate.strftime('%d')

    # (2., 5. render .html page)
    return render(request,
                  'checkPointMng/las.html',
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
    # data = {
    #     '2015': {
    #         'data': [],
    #         'labels': [],
    #     },
    #     '2016': {
    #         'data': [],
    #         'labels': [],
    #     },
    #     '2017': {
    #         'data': [],
    #         'labels': []
    #     },
    #     '2018': {
    #         'data': [],
    #         'labels': []
    #     },
    #     '2019': {
    #         'data': [],
    #         'labels': []
    #     },
    #     '2020': {
    #         'data': [],
    #         'labels': []
    #     },
    #     'prediction': {
    #         'data': [],
    #         'labels': []
    #     }
    # }

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

            # LA_Data = pd.read_csv('checkPoint/static/Merged_Data/LAX_' + terminal + '.csv',
            #                       header=0,
            #                       squeeze=True)
            # date_str = 'Date'
            # throughput_str = 'PMIS - Total Customer Throughput (Unadjusted)'
            # year_symbols = {
            #     '2015': '_x',
            #     '2016': '_y',
            #     '2017': '_x.1',
            #     '2018': '_y.1',
            #     '2019': '',
            # }
            #
            # for i in range(2015, 2020):
            #     LA_Data['date' + str(i)] = LA_Data[date_str + year_symbols[str(i)]].astype(str)
            #     LA_Data['date' + str(i)] = pd.to_datetime(LA_Data['date' + str(i)], format='%Y-%m-%d')
            #     LA_Data['throughput' + str(i)] = LA_Data[throughput_str + year_symbols[str(i)]]
            #
            # filtered_data = LA_Data[(LA_Data['date' + startYear] >= startDate) & (LA_Data['date' + startYear] <= endDate)]
            #
            # for i in range(2015, 2020):
            #     new_filtered_data = filtered_data[['date' + str(i), 'throughput' + str(i), 'Hour']].dropna()
            #     new_filtered_data = new_filtered_data.sort_values(by=['date' + str(i), 'Hour'])
            #     data[str(i)]['data'] = new_filtered_data['throughput' + str(i)].tolist()
            #     labels = []
            #     for index, row in new_filtered_data.iterrows():
            #         date = row['date' + str(i)]
            #         time = row['Hour']
            #         date_time = datetime.datetime.combine(date, datetime.time.fromisoformat(time))
            #         labels.append(date_time.strftime("%m/%d/%Y %H:%M:%S"))
            #     data[str(i)]['labels'] = labels
            #
            # prediction_data = filtered_data[['date2015', 'throughput2015', 'date2016', 'throughput2016', 'date2017', 'throughput2017', 'date2018', 'throughput2018', 'date2019', 'throughput2019', 'Hour']].dropna()
            # prediction_data = prediction_data.sort_values(by=['date2015', 'Hour'])
            # prediction_labels = []
            # predicted_values = []
            # data_2019 = []
            #
            # for index, row in prediction_data.iterrows():
            #     org_data = [row['throughput2015'], row['throughput2016'], row['throughput2017'], row['throughput2018']]
            #     ARIMA_Model = ARIMA(org_data, order=(1, 1, 0))
            #     Model_Fit = ARIMA_Model.fit()
            #     Predict_Value = Model_Fit.forecast()
            #     date = row['date2019']
            #     time = row['Hour']
            #     date_time = datetime.datetime.combine(date, datetime.time.fromisoformat(time))
            #     predicted_values.append(Predict_Value)
            #     prediction_labels.append(date_time.strftime("%m/%d/%Y %H:%M:%S"))
            #     data_2019.append(row['throughput2019'])
            #
            # data['2019']['labels'] = prediction_labels
            # data['prediction']['labels'] = prediction_labels
            # data['2019']['data'] = data_2019
            # data['prediction']['data'] = predicted_values




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
                      # 'data': data,
                  })


# PHX airport home page
def phx(request):
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
        form = PHXDayForm(request.POST, request.FILES)

        # if valid, save form and return with GET parameter
        if form.is_valid():
            terminal = request.POST.get('terminal')
            start = request.POST.get('start')
            end = request.POST.get('end')

            return HttpResponseRedirect('/phx?submitted=True&terminal=' + terminal + '&start=' + start + '&end=' + end)

    # else (GET) (1. display an empty form to be filled out for the first time),
    else:
        form = PHXDayForm()

        # if (4. submitted is passed as GET parameter, set submitted to true)
        if 'submitted' in request.GET:
            submitted = True
            terminal = request.GET.get('terminal')
            start = request.GET.get('start')
            end = request.GET.get('end')
            startDate = datetime.datetime.strptime(start, '%m/%d/%Y')
            endDate = datetime.datetime.strptime(end, '%m/%d/%Y')

            # to utilize ISO calendar - startDate.year/month/day

            startYear = startDate.strftime('%Y')
            startMonth = startDate.strftime('%m')
            startDay = startDate.strftime('%d')
            endYear = endDate.strftime('%Y')
            endMonth = endDate.strftime('%m')
            endDay = endDate.strftime('%d')

    # (2., 5. render .html page)
    return render(request,
                  'checkPointMng/phx.html',
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


# data preparation page
def datapreparation(request):
    return render(request,
                  'checkPointMng/datapreparation.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


# passenger forecasting page
def passengerforecasting(request):
    return render(request,
                  'checkPointMng/passengerforecasting.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })
