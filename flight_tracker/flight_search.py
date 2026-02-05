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

    def get_current_price(self, origin, destination, departure_date):
        """
        Returns cheapest flight price
        """
        if self.amadeus:
            try:
                response = self.amadeus.shopping.flight_offers_search.get(
                    originLocationCode=origin,
                    destinationLocationCode=destination,
                    departureDate=departure_date,
                    adults=1,
                    max=1,
                    currencyCode="INR"
                )

                if response.data:
                    return float(response.data[0]["price"]["grandTotal"])

            except ResponseError as error:
                print(f"Amadeus API Error: {error}")

        return self._fallback_price(origin, destination)

    def _fallback_price(self, origin, destination):
        print("Using mock data...")
        if os.path.exists(self.mock_data_file):
            with open(self.mock_data_file, "r") as f:
                mock_data = json.load(f)
                route = f"{origin}-{destination}"
                return mock_data.get(route, float('inf'))
        return float('inf')
