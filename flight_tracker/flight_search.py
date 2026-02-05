import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")
AMADEUS_TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_SEARCH_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    def __init__(self, mock_data_file="mock_prices.json"):
        self.mock_data_file = mock_data_file
        self._token = None

    def _get_new_token(self):
        if not AMADEUS_API_KEY or not AMADEUS_API_SECRET:
            print("Missing Amadeus API credentials.")
            return None

        response = requests.post(
            AMADEUS_TOKEN_URL,
            data={
                "grant_type": "client_credentials",
                "client_id": AMADEUS_API_KEY,
                "client_secret": AMADEUS_API_SECRET
            }
        )
        if response.status_code == 200:
            return response.json().get("access_token")
        else:
            print(f"Error getting token: {response.status_code} {response.text}")
            return None

    def get_current_price(self, origin, destination, departure_date=None):
        if not self._token:
            self._token = self._get_new_token()

        if self._token:
            params = {
                "originLocationCode": origin,
                "destinationLocationCode": destination,
                "departureDate": departure_date,
                "adults": 1,
                "max": 1,
                "currencyCode": "USD"
            }
            headers = {"Authorization": f"Bearer {self._token}"}
            response = requests.get(AMADEUS_SEARCH_URL, params=params, headers=headers)

            if response.status_code == 200:
                data = response.json()
                if data["data"]:
                    return float(data["data"][0]["price"]["grandTotal"])
                else:
                    print(f"No flight offers found for {origin} -> {destination} on {departure_date}.")
            elif response.status_code == 401:
                self._token = self._get_new_token()
                if self._token:
                    return self.get_current_price(origin, destination, departure_date)
            else:
                print(f"Amadeus API Error: {response.status_code} {response.text}")

        # Fallback to mock data
        print("Falling back to mock data...")
        if os.path.exists(self.mock_data_file):
            with open(self.mock_data_file, "r") as f:
                mock_data = json.load(f)
                route = f"{origin}-{destination}"
                return mock_data.get(route, float('inf'))
        return float('inf')

    def get_destination_code(self, city_name):
        return city_name.upper()[:3]
