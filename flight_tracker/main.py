from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

def main():
    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    alerts = data_manager.get_alerts()

    for alert in alerts:
        origin = alert["origin"]
        destination = alert["destination"]
        target_price = alert["target_price"]
        departure_date = alert.get("departure_date")

        print(f"Checking flights for {origin} -> {destination} on {departure_date}...")
        current_price = flight_search.get_current_price(origin, destination, departure_date)

        if current_price <= target_price:
            notification_manager.send_alert(origin, destination, current_price, target_price)
        else:
            print(f"Current price ${current_price} is still above target ${target_price}.")

if __name__ == "__main__":
    main()
