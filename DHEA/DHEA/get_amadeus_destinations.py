# import requests
# import itertools
# import json
# import sys


# AMADEUS_SEARCH_URL = "https://test.api.amadeus.com/v1/reference-data/locations/"
# AMADEUS_ACCESS_TOKEN = 'nkYdoZJEweZOJuDvycYqUMAPqnT5'


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
# 			'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
# 			'y', 'z']
# CITIES = ['Rome', 'Singapore', 'Madrid', 'Oslo', 'Lisbon', 'London', 'Dublin', 'Bogota', 'Stockholm', 'Jerusalem', 'Toronto', 'Helsinki', 'Sydney', 'Santiago', 'Copenhagen', 'San Jose', 'Boston', 'Ljubljana', 'Wellington', 'Bangkok', 'Kuala Lumpur', 'Warsaw', 'Budapest', 'Istanbul', 'Tallinn', 'Amman', 'Mexico City', 'Seoul', 'New Delhi', 'Hanoi']
# CODES  = ['FCO', 'SIN', 'MAD', 'OSL', 'LIS', 'LCY', 'DUB', 'BOG', 'ARN', 'JRS', 'YYZ', 'HEL', 'SYD', 'SCL', 'CPH', 'SJO', 'BOS', 'LJU', 'WLG', 'BKK', 'KUL', 'WAW', 'BUD', 'IST', 'TLL', 'AMM', 'MEX', 'ICN', 'DEL', 'HAN']

# PAGE_LIMIT = 5


# def main():

# 	headers = { 
# 		"Authorization": 'Bearer ' + AMADEUS_ACCESS_TOKEN
# 	}

# 	links = []
# 	for code in CODES:
# 		r = requests.get(AMADEUS_SEARCH_URL + 'C' + code,
# 						headers = headers)
# 		print("STATUS CODE: " + str(r.status_code))

# 	# print(str(links))


# if __name__ == "__main__":
# 	main()


import requests
import itertools
import json
import sys


AMADEUS_SEARCH_URL = "https://test.api.amadeus.com/v1/reference-data/locations"
AMADEUS_ACCESS_TOKEN = 'Y9osVfJ1J1UrBnhfgzfs8jNz4D7B'

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
			'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
			'y', 'z']
PAGE_LIMIT = 300


def main():

	headers = { 
		"Authorization": 'Bearer ' + AMADEUS_ACCESS_TOKEN
	}

	codes = []
	for letter in alphabet:
		body = "?subType=CITY&keyword=" + letter + "&page[limit]=" + str(PAGE_LIMIT)

		r = requests.get(AMADEUS_SEARCH_URL + body, 
						 headers=headers)

		codes.append([(d['iataCode'], d['address']['countryName']) for d in r.json()['data']])

	print("codes: " + str(list(set(itertools.chain.from_iterable(codes)))))


if __name__ == "__main__":
	main()