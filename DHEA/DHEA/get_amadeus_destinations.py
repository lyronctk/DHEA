import requests
import itertools
import json
import sys


AMADEUS_SEARCH_URL = "https://test.api.amadeus.com/v1/reference-data/locations"
AMADEUS_ACCESS_TOKEN = 'Aw3VklcCfniYIq6wXK9AVAEFEycW'

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
			'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
			'y', 'z']
PAGE_LIMIT = 50


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