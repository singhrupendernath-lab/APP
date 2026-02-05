# Flight Fare Alert System

A Python-based tool to track flight prices and receive alerts when they drop below a specified threshold.

## Features

- **Alert Management**: Add flight routes and target prices via a simple Command Line Interface (CLI).
- **Price Monitoring**: Check current flight prices against your set targets.
- **Notifications**: Get notified via console output and a persistent log file (`flight_alerts.log`) when a deal is found.
- **Modular Design**: Easy to extend or integrate with real-world flight APIs (e.g., Amadeus, Tequila).

## Project Structure

- `flight_tracker/`: Core package containing the application logic.
  - `cli.py`: Command Line Interface to add new alerts.
  - `main.py`: Main entry point to run the monitoring logic.
  - `data_manager.py`: Handles loading and saving flight alerts.
  - `flight_search.py`: Handles flight price searching (currently uses mock data).
  - `notification_manager.py`: Manages alerting the user.
- `alerts.json`: Persistent storage for your flight alerts.
- `mock_prices.json`: Mock data source for flight prices used by `FlightSearch`.
- `flight_alerts.log`: Log file where all detected low-price alerts are saved.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone or download this project.
2. (Optional) Install dependencies if you decide to extend the project with real APIs:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Adding a Flight Alert

Use the `cli.py` script to set a new alert. Provide the origin airport code, destination airport code, and your target price.

```bash
PYTHONPATH=flight_tracker python3 flight_tracker/cli.py <ORIGIN> <DESTINATION> <TARGET_PRICE>
```

**Example:**
```bash
PYTHONPATH=flight_tracker python3 flight_tracker/cli.py LHR JFK 500
```

### 2. Checking for Price Drops

Run the `main.py` script to check all your saved alerts against the "current" prices.

```bash
PYTHONPATH=flight_tracker python3 flight_tracker/main.py
```

If a flight's current price is less than or equal to your target price, you will see an alert on your console and it will be recorded in `flight_alerts.log`.

### 3. Testing with Mock Data

The project currently uses `mock_prices.json` to simulate flight prices. You can edit this file to test the alerting system:

```json
{
    "LHR-JFK": 450.0,
    "SFO-CDG": 800.0,
    "SYD-TYO": 600.0
}
```

If you add an alert for `LHR` to `JFK` with a target price of `500`, running `main.py` will trigger an alert because the mock price is `450`.

## Future Improvements

- Integrate with live Flight APIs (like Kiwi Tequila or Amadeus).
- Add email or SMS notifications using Twilio or SMTP.
- Support for specific dates or date ranges.
