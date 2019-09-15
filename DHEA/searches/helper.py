from datetime import datetime
from dateutil.parser import parse
from datetime import timedelta

import requests
import json


AMADEUS_ACCESS_TOKEN = 'kYHoYatMF5as3EpJVjExycsqXBEA'
FLIGHT_OFFERS_URL = "https://test.api.amadeus.com/v1/shopping/flight-offers"
NUM_FLIGHTS = 20


def get_price_with_tax(response):
	price_dumps = [response.json()['data'][i]['offerItems'][0]['price'] for i in range(NUM_FLIGHTS)]
	with_taxes = [float(pd['total']) + float(pd['totalTaxes']) for pd in price_dumps]

	return min(with_taxes)


def date_time_to_str(dt):
	return dt.strftime("%Y") + '-' + \
		   dt.strftime("%m") + '-' + \
		   dt.strftime("%d")


def get_return_date(departure_date, avg_recovery_time):
	return_date = departure_date + timedelta(days=avg_recovery_time)

	return date_time_to_str(return_date)


def concat_offers_params(origin, destination, departure_date, return_date):
	departure_date_str = date_time_to_str(departure_date)

	param_origin         = 'origin=' + origin
	param_destination    = 'destination=' + destination
	param_departure_date = 'departureDate=' + departure_date_str
	param_return_date    = 'returnDate=' + return_date
	param_currency       = 'currency=USD'
	param_max_result     = 'max=' + str(NUM_FLIGHTS)

	return '?' +  \
		param_origin + '&' +  \
		param_destination + '&' +  \
		param_departure_date  + '&' + \
		param_return_date + '&' + \
		param_currency + '&' + \
		param_max_result


def get_cheapest_travel(origin, destination, departure_date, avg_recovery_time):
	
	return_date = get_return_date(departure_date, avg_recovery_time)

	headers = { 
		"Authorization": 'Bearer ' + AMADEUS_ACCESS_TOKEN
	}

	body = concat_offers_params(origin, destination, 
							departure_date, return_date)


	r = requests.get(FLIGHT_OFFERS_URL + body, 
					 headers=headers)

	# print("===================")
	# print("BODY: " + str(body))
	# print("RESPONSE: " + str(r))
	# print("===================")

	return get_price_with_tax(r)

