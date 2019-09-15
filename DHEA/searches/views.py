# Knee replacement
# DEL
# 2019-10-15

# PTCA
# BOS
# 2020-01-15

from django.http import HttpResponse
from django.shortcuts import render

from .models import Country
from .models import Procedure

from .helper import get_cheapest_travel

from datetime import datetime
from dateutil.parser import parse
from datetime import timedelta


def home(request):
    return render(request, 'home.html')


def results(request):
	procedure = request.GET.get('procedure', '')
	city      = request.GET.get('city', '')
	date      = request.GET.get('datepicker', '')

	OPERATION_NAME_HOLDER = procedure
	DEPARTURE_STR_HOLDER  = date
	ORIGIN_HOLDER         = city

	origin_country   = Country.objects.get(city=ORIGIN_HOLDER)
	origin_procedure = Procedure.objects.get(name=OPERATION_NAME_HOLDER, country=origin_country)

	departure = datetime.strptime(DEPARTURE_STR_HOLDER, '%Y-%m-%d')

	cards = []
	for current_country in Country.objects.all():
		if current_country == origin_country:
			continue

		card = {}

		current_procedure = Procedure.objects.get(name=OPERATION_NAME_HOLDER, country=current_country)

		card['country_name']   = current_country.name
		card['nightly_cost']   = current_country.avg_per_night_cost
		card['procedure_cost'] = current_procedure.avg_procedure_cost
		card['recovery_time']  = current_procedure.avg_recovery_time
		card['travel_cost']    = int(get_cheapest_travel(origin_country.city, current_country.city, 
									departure, current_procedure.avg_recovery_time))

		card['wait_time']    = current_procedure.avg_waiting_time
		card['quality_rank'] = current_country.quality_rank

		card['total_cost']   = (card['nightly_cost'] * card['recovery_time']) + card['procedure_cost'] + card['travel_cost']
		card['total_cost'] = int(card['total_cost'])

		card['hospital_1_name'] = current_country.hospital_1_name
		card['hospital_2_name'] = current_country.hospital_2_name
		card['hospital_3_name'] = current_country.hospital_3_name

		card['hospital_1_link'] = current_country.hospital_1_link
		card['hospital_2_link'] = current_country.hospital_2_link
		card['hospital_3_link'] = current_country.hospital_3_link

		cards.append(card)


	return render(request, 'results.html', {'cards': cards,
											'operation_name': OPERATION_NAME_HOLDER,
											'target_date': DEPARTURE_STR_HOLDER,
											'origin_country_name': origin_country.name,
											'origin_procedure_wait': origin_procedure.avg_waiting_time,
											'origin_country_quality': origin_country.quality_rank,
											'origin_total_cost': (origin_country.avg_per_night_cost * origin_procedure.avg_recovery_time) + origin_procedure.avg_procedure_cost})

