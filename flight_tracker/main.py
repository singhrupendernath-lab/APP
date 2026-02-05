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
        offers = flight_search.get_current_price(origin, destination, departure_date)

        if offers:
            # Assuming offers are sorted by price from the API
            cheapest_offer = offers[0]
            current_price = cheapest_offer["price"]
            currency = cheapest_offer["currency"]

            if current_price <= target_price:
                notification_manager.send_alert(origin, destination, target_price, offers)
            else:
                print(f"Current lowest price {currency} {current_price} is still above target {target_price}.")
        else:
            print(f"No offers found for {origin} -> {destination}")

if __name__ == "__main__":
    main()
