from django.shortcuts import render
from django.http import HttpResponse

def browseSalads(request):
    return render(request, 'salidify/browseSalads.html')

def similarSalads(request):
    return render(request, 'salidify/similarSalads.html')

def browseFilter(request):
    return render(request, 'salidify/browseFilter.html')

def viewIngredients(request):
    return render(request, 'salidify/viewIngredients.html')

def shopIngredients(request):
    return render(request, 'salidify/shopIngredients.html')

def alternateIngredients(request):
    return render(request, 'salidify/alternateIngredients.html')

def viewInstructions(request):
    return render(request, 'salidify/viewInstructions.html')

def index(request):
    return render(request, 'salidify/index.html')
