import json
import os
from amadeus import Client, ResponseError
from dotenv import load_dotenv

load_dotenv()

AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")


class FlightSearch:
    def __init__(self, mock_data_file="mock_prices.json"):
        self.mock_data_file = mock_data_file
        if AMADEUS_API_KEY and AMADEUS_API_SECRET:
            self.amadeus = Client(
                client_id=AMADEUS_API_KEY,
                client_secret=AMADEUS_API_SECRET
            )
        else:
            self.amadeus = None
            print("Missing Amadeus API credentials. SDK not initialized.")

    def get_iata_code(self, city):
        if not self.amadeus:
            return city.upper()[:3]

        try:
            response = self.amadeus.reference_data.locations.get(
                keyword=city,
                subType='CITY'
            )
            if response.data:
                return response.data[0]['iataCode']
            else:
                print(f"No IATA code found for city: {city}")
                return city.upper()[:3]
        except ResponseError as error:
            print(f"Amadeus API Error (Locations): {error}")
            return city.upper()[:3]

    def get_current_price(self, origin, destination, departure_date=None):
        offers = []
        if self.amadeus:
            try:
                response = self.amadeus.shopping.flight_offers_search.get(
                    originLocationCode=origin,
                    destinationLocationCode=destination,
                    departureDate=departure_date,
                    adults=1,
                    max=5,
                    currencyCode="USD"
                )

                if response.data:
                    dictionaries = response.result.get('dictionaries', {})
                    carriers = dictionaries.get('carriers', {})

                    for offer in response.data:
                        price = float(offer["price"]["grandTotal"])
                        currency = offer["price"]["currency"]
                        carrier_code = offer["validatingAirlineCodes"][0]
                        airline_name = carriers.get(carrier_code, carrier_code)

                        offers.append({
                            "price": price,
                            "currency": currency,
                            "airline": airline_name
                        })
                    return offers
                else:
                    print(f"No flight offers found for {origin} -> {destination} on {departure_date}.")
            except ResponseError as error:
                print(f"Amadeus API Error (Flight Offers): {error}")

        # Fallback to mock data
        if not offers:
            print("Falling back to mock data...")
            if os.path.exists(self.mock_data_file):
                with open(self.mock_data_file, "r") as f:
                    mock_data = json.load(f)
                    route = f"{origin}-{destination}"
                    price = mock_data.get(route, float('inf'))
                    offers.append({
                        "price": price,
                        "currency": "USD",
                        "airline": "Mock Airline"
                    })
            else:
                offers.append({
                    "price": float('inf'),
                    "currency": "USD",
                    "airline": "Unknown"
                })
        return offers
