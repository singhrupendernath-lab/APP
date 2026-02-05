import json
import os
from datetime import datetime, timedelta

class DataManager:
    def __init__(self, filename="alerts.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def get_alerts(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error reading {self.filename}: {e}. Returning an empty list of alerts.")
            return []

    def add_alert(self, origin, destination, target_price, departure_date=None):
        if not departure_date:
            # Default to 30 days from now
            departure_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")

        alerts = self.get_alerts()
        new_alert = {
            "origin": origin,
            "destination": destination,
            "target_price": float(target_price),
            "departure_date": departure_date
        }
        alerts.append(new_alert)
        try:
            with open(self.filename, "w") as f:
                json.dump(alerts, f, indent=4)
        except Exception as e:
            print(f"Error writing to {self.filename}: {e}")
        return new_alert
