# Flight Fare Alert System

A Python-based tool to track flight prices and receive alerts when they drop below a specified threshold. Now integrated with the Amadeus Flight API!

## Features

- **Alert Management**: Add flight routes, target prices, and departure dates via a simple CLI.
- **Price Monitoring**: Check current flight prices using the Amadeus Flight API.
- **Notifications**: Get notified via console output and a persistent log file (`flight_alerts.log`).
- **Modular Design**: Easy to extend or integrate with other notifications like email or SMS.

## Project Structure

- `flight_tracker/`: Core package containing the application logic.
  - `cli.py`: Command Line Interface to add new alerts.
  - `main.py`: Main entry point to run the monitoring logic.
  - `data_manager.py`: Handles loading and saving flight alerts.
  - `flight_search.py`: Handles flight price searching using Amadeus API.
  - `notification_manager.py`: Manages alerting the user.
- `alerts.json`: Persistent storage for your flight alerts.
- `.env`: Store your Amadeus API credentials here (ignored by git).
- `mock_prices.json`: Fallback mock data source.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone or download this project.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### API Configuration

1. Get your Amadeus API Key and Secret from the [Amadeus for Developers portal](https://developers.amadeus.com/).
2. Create a `.env` file in the root directory (or copy from `.env.example`):
   ```bash
   cp .env.example .env
   ```
3. Add your credentials to the `.env` file:
   ```
   AMADEUS_API_KEY=YOUR_API_KEY
   AMADEUS_API_SECRET=YOUR_API_SECRET
   ```

## Usage

### 1. Adding a Flight Alert

Use the `cli.py` script to set a new alert. Provide the origin airport code, destination airport code, target price, and an optional departure date.

```bash
PYTHONPATH=flight_tracker python3 flight_tracker/cli.py <ORIGIN> <DESTINATION> <TARGET_PRICE> [DEPARTURE_DATE (YYYY-MM-DD)]
```

**Example:**
```bash
PYTHONPATH=flight_tracker python3 flight_tracker/cli.py LHR JFK 500 2024-12-15
```
*If no date is provided, it defaults to 30 days from today.*

### 2. Checking for Price Drops

Run the `main.py` script to check all your saved alerts against the Amadeus API.

```bash
PYTHONPATH=flight_tracker python3 flight_tracker/main.py
```

If a flight's current price is less than or equal to your target price, an alert will be triggered.

## Testing with Mock Data

If no API keys are provided in the `.env` file, the system will fall back to using `mock_prices.json`.
