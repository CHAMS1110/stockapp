from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponse
from .forms import TickerForm, PriceSearchForm
from .tiingo import get_meta_data, get_price_data, get_histo_price_data
import pandas as pd
from datetime import date, timedelta
import requests
import json



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def test(request):
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker)
    else:
        form = TickerForm()
    return render(request, 'home/stocks.html', {'form': form})


@login_required(login_url="/login/")
def ticker(request, tid):
    context = {}
    context['ticker'] = tid
    context['meta'] = get_meta_data(tid)
    context['price'] = get_price_data(tid)
    return render(request, 'home/chart.html', context)


@login_required(login_url="/login/")
def chart(request, tid):
    response = None
    date_from = None
    date_to = None
    wrong_input = None
    search_form = PriceSearchForm(request.POST or None)   
    #get post request from the front end
    if request.method == 'POST': 
        if search_form.is_valid():   
        #Confirm if valid data was received from the form
            date_from = request.POST.get('date_from') 
            #extract input 1 from submitted data
            date_to = request.POST.get('date_to')  
            #extract input 2 from submitted data
        else:
            raise Http400("Sorry, this did not work. Invalid input")

        api = 'https://api.tiingo.com/tiingo/daily/aapl/prices?startDate='+ date_from +'&endDate='+ date_to +'&token=96f4a5ea160a345defdfff0320144e7c469ce70f'
        if date_to > date_from:     
        #confirm that input2 is greater than inp t 1
            try:
                response = requests.get(api).json() 
            except requests.exceptions.ConnectionError as errc:
        #raise error if connection fails
                raise ConnectionError(errc)
            except requests.exceptions.Timeout as errt:   
        # raise error if the request gets timed out without receiving a single byte
                raise TimeoutError(errt)
            except requests.exceptions.HTTPError as err:   
        # raise a general error if the above named errors are not triggered 
                raise SystemExit(err)
        else:
            wrong_input = 'Wrong date input selection: date from cant be greater than date to, please try again' 
        #print out an error message if the user chooses a date that is greater than input1's date 
    context = {
        'Tresponse':response,
        'search_form':search_form,
        'wrong_input' : wrong_input,
        'date_from': date_from,
        'date_to': date_to,
        }
    context['ticker'] = tid
    context['meta'] = get_meta_data(tid)
    context['price'] = get_price_data(tid)
    return render(request, 'home/chart.html', context)

@login_required(login_url="/login/")
def page_dash(request):
    return render(request, 'home/dashboard.html')
    
@login_required(login_url="/login/")
def page_trans(request):
    return render(request, 'home/transactions.html')
    
    
