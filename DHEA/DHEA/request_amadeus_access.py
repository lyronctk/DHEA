import requests
import json
import sys

# @@param[0] == API_KEY
# @@param[1] == API_SECRET


AMADEUS_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"

def main():
	API_KEY = sys.argv[1]
	API_SECRET = sys.argv[2]


	headers = { 
		"Content-Type": "application/x-www-form-urlencoded"
	}
	body = "grant_type=client_credentials&client_id=" + API_KEY + "&client_secret=" + API_SECRET


	r = requests.post(AMADEUS_URL, 
					  headers=headers, 
					  data=body)

	print("")
	print("AMADEUS_ACCESS_TOKEN: "+ 
		r.json()['access_token'])


if __name__ == "__main__":
	main()