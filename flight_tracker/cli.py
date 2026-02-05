import sys
from data_manager import DataManager
from flight_search import FlightSearch

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 cli.py <ORIGIN_CITY/IATA> <DESTINATION_CITY/IATA> <TARGET_PRICE> [DEPARTURE_DATE (YYYY-MM-DD)]")
        return

    origin_input = sys.argv[1]
    destination_input = sys.argv[2]
    target_price = sys.argv[3]
    departure_date = sys.argv[4] if len(sys.argv) > 4 else None

    flight_search = FlightSearch()

    # Resolve city names to IATA codes if necessary
    print(f"Resolving IATA codes for {origin_input} and {destination_input}...")
    origin = flight_search.get_iata_code(origin_input)
    destination = flight_search.get_iata_code(destination_input)

    data_manager = DataManager()
    alert = data_manager.add_alert(origin, destination, target_price, departure_date)
    print(f"Added alert: {alert['origin']} -> {alert['destination']} on {alert['departure_date']} at ${alert['target_price']}")

if __name__ == "__main__":
    main()
