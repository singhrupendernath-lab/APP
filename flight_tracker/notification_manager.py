class NotificationManager:
    def send_alert(self, origin, destination, price, target_price):
        message = f"ALERT! Low price detected for {origin} -> {destination}!\n" \
                  f"Current price: ${price}\n" \
                  f"Target price: ${target_price}\n" \
                  f"Go book your flight now!"
        print(message)
        with open("flight_alerts.log", "a") as f:
            f.write(message + "\n" + "-"*20 + "\n")
