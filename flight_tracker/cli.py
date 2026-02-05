import sys
from data_manager import DataManager

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 cli.py <ORIGIN> <DESTINATION> <TARGET_PRICE>")
        return

    origin = sys.argv[1].upper()
    destination = sys.argv[2].upper()
    target_price = sys.argv[3]

    data_manager = DataManager()
    alert = data_manager.add_alert(origin, destination, target_price)
    print(f"Added alert: {alert['origin']} -> {alert['destination']} at ${alert['target_price']}")

if __name__ == "__main__":
    main()
