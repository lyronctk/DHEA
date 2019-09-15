from django.http import HttpResponse
from django.shortcuts import render
from .models import Country


def home(request):
    return HttpResponse('Hello, World!')


def results(request):
    countries = Country.objects.all()
    return render(request, 'results.html', {'countries': countries})