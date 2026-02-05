class NotificationManager:
    def send_alert(self, origin, destination, target_price, offers):
        cheapest_offer = offers[0]
        message = f"ALERT! Low price detected for {origin} -> {destination}!\n" \
                  f"Target price: {target_price}\n\n" \
                  f"Flight Offers:\n"

        for offer in offers:
            message += f"- {offer['airline']}: {offer['currency']} {offer['price']}\n"

        message += f"\nGo book your flight now!"

        print(message)
        with open("flight_alerts.log", "a") as f:
            f.write(message + "\n" + "-"*20 + "\n")
