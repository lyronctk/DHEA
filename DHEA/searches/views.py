from django.http import HttpResponse
from django.shortcuts import render

from .models import Country
from .helper import get_cheapest_travel

from datetime import datetime
from dateutil.parser import parse
from datetime import timedelta


def home(request):
    return HttpResponse('Hello, World!')


def results(request):
    countries = Country.objects.all()

    departure = datetime.strptime('2020-08-01', '%Y-%m-%d')
    cheapest_travel = get_cheapest_travel('NYC', 'MAD', departure, 40)

    print("LOWEST PRICE: " + str(cheapest_travel))

    return render(request, 'results.html', {'countries': countries})