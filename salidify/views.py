from django.shortcuts import render
from django.http import HttpResponse

def forecast(request):
    return render(request, 'salidify/screen1.html')

def forecast_alert(request):
    return render(request, 'salidify/screen2.html')

def comparison(request):
    return render(request, 'salidify/screen3.html')

def comparison_alert(request):
    return render(request, 'salidify/screen4.html')

def index(request):
    return render(request, 'salidify/index.html')