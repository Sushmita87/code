from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect
 
from chartss.models import City
from iexfinance.stocks import get_historical_data
from datetime import datetime, timedelta
import json
 
def home(request):

    end = datetime.now()
    start = end - timedelta(days=30)
    stock_name = request.GET.get('stock_name','TSLA')
    start_date = request.GET.get('start_date')
    if start_date:
        start_date = start_date.split('T')[0]
        start_date = start_date.split('-')
        start = datetime(int(start_date[0]),int(start_date[1]),int(start_date[2]))
    end_date = request.GET.get('end_date')
    if end_date:
        end_date = end_date.split('T')[0]
        end_date = end_date.split('-')
        end = datetime(int(end_date[0]),int(end_date[1]),int(end_date[2]))
    df = get_historical_data(stock_name, start, end,
                              token="pk_02bb12d2614541f9a993f88b91c20228")
    data = dict(df.close)

    x_data = [timestamp.strftime('%y-%m-%d %H:%M:%S') for timestamp in data.keys()]
    y_data = list(data.values())
    return render(request, 'home.html', context={'x_data':json.dumps(x_data),
                                                 'y_data': json.dumps(y_data)})
 
def pie_chart(request):
    labels = []
    data = []
 
    queryset = City.objects.order_by('-population')[:9]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)
 
    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })