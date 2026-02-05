import json
import os

class DataManager:
    def __init__(self, filename="alerts.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def get_alerts(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def add_alert(self, origin, destination, target_price):
        alerts = self.get_alerts()
        new_alert = {
            "origin": origin,
            "destination": destination,
            "target_price": float(target_price)
        }
        alerts.append(new_alert)
        with open(self.filename, "w") as f:
            json.dump(alerts, f, indent=4)
        return new_alert
