import json
import os

class FlightSearch:
    def __init__(self, mock_data_file="mock_prices.json"):
        self.mock_data_file = mock_data_file

    def get_current_price(self, origin, destination):
        # In a real application, this would call a flight search API like Tequila or Amadeus.
        # For this demonstration, we use a mock data source.
        if os.path.exists(self.mock_data_file):
            with open(self.mock_data_file, "r") as f:
                mock_data = json.load(f)
                route = f"{origin}-{destination}"
                return mock_data.get(route, float('inf'))
        else:
            print(f"Mock data file {self.mock_data_file} not found. Returning infinity.")
            return float('inf')

    def get_destination_code(self, city_name):
        # Real implementation would use a Locations API to get IATA codes.
        # This is a placeholder.
        return city_name.upper()[:3]
