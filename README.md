# Flight Fare Alert System

A Python-based tool to track flight prices and receive alerts when they drop below a specified threshold. Integrated with the official Amadeus Flight API Python SDK!

## Features

- **Alert Management**: Add flight routes using either **City Names** (e.g., "London") or **IATA Codes** (e.g., "LHR").
- **Automatic Code Resolution**: Automatically converts city names to their corresponding IATA codes using the Amadeus Locations API.
- **Price Monitoring**: Check real-time flight prices using the official Amadeus Python SDK.
- **Notifications**: Get notified via console output and a persistent log file (`flight_alerts.log`).
- **Modular Design**: Clean separation of concerns between data storage, flight searching, and notifications.

## Project Structure

- `flight_tracker/`: Core package containing the application logic.
  - `cli.py`: Command Line Interface to add new alerts. Supports city names.
  - `main.py`: Main entry point to run the monitoring logic.
  - `data_manager.py`: Handles loading and saving flight alerts in `alerts.json`.
  - `flight_search.py`: Handles flight price searching and IATA code resolution using the `amadeus` Python SDK.
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

Use the `cli.py` script to set a new alert. You can provide airport IATA codes OR city names.

```bash
PYTHONPATH=flight_tracker python3 flight_tracker/cli.py <ORIGIN_CITY/IATA> <DESTINATION_CITY/IATA> <TARGET_PRICE> [DEPARTURE_DATE (YYYY-MM-DD)]
```

**Examples:**
```bash
# Using IATA codes
PYTHONPATH=flight_tracker python3 flight_tracker/cli.py LHR JFK 500 2026-06-01

# Using city names
PYTHONPATH=flight_tracker python3 flight_tracker/cli.py London Paris 200
```
*If no date is provided, it defaults to 30 days from today.*

### 2. Checking for Price Drops

Run the `main.py` script to check all your saved alerts. This script will call the Amadeus API for each alert and notify you if a price drop is detected.

```bash
PYTHONPATH=flight_tracker python3 flight_tracker/main.py
```

## Testing with Mock Data

If no API keys are provided in the `.env` file, the system will fall back to using `mock_prices.json`.
