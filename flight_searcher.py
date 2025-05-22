import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearcher:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._amadeus_api_key = os.environ.get("AMADEUS_API_KEY")
        self._amadeus_api_secret = os.environ.get("AMADEUS_API_SECRET")
        self._token = self._get_new_token()

    def _get_new_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._amadeus_api_key,
            "client_secret": self._amadeus_api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=body)
        response.raise_for_status()
        json = response.json()
        return json["access_token"]

    def check_new_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": 10,
        }
        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=query)
        response.raise_for_status()
        return response.json()
