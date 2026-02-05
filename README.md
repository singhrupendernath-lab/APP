# Flight Fare Alert System

A Python-based tool to track flight prices and receive alerts when they drop below a specified threshold. Integrated with the official Amadeus Flight API Python SDK!

## Features

- **Alert Management**: Add flight routes using either **City Names** (e.g., "London") or **IATA Codes** (e.g., "LHR").
- **Automatic Code Resolution**: Automatically converts city names to their corresponding IATA codes.
- **Price Monitoring**: Check real-time flight prices using the official Amadeus Python SDK.
- **Notifications**: Get notified via console output and a persistent log file (`flight_alerts.log`).
- **Currency Support**: Displays the currency code returned by the API (e.g., USD, INR).

## Amadeus Test API Limitations

If you are using an Amadeus **Test** API key, please be aware of the following:

1.  **Limited/Simulated Data**: The test environment does not have access to live real-time flight data for all routes. It often returns static or simulated results, which may result in the **same price** being shown for different dates.
2.  **Date Windows**: Most airlines publish their flight schedules approximately **330 to 360 days** in advance. If you search for dates beyond this window, the API may return an error or no results.
3.  **Currency**: While the system requests USD, the API may return prices in the local currency of the departure/destination country in certain test scenarios. The system now correctly identifies and displays the currency returned by the API.

## Project Structure

- `flight_tracker/`: Core package containing the application logic.
  - `cli.py`: Command Line Interface to add new alerts.
  - `main.py`: Main entry point to run the monitoring logic.
  - `data_manager.py`: Handles loading and saving flight alerts.
  - `flight_search.py`: Handles API interactions.
  - `notification_manager.py`: Manages alerting the user.
- `alerts.json`: Persistent storage for your flight alerts.
- `.env`: Store your Amadeus API credentials here.

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

1. Get your Amadeus API credentials from the [Amadeus for Developers portal](https://developers.amadeus.com/).
2. Create a `.env` file and add your credentials:
   ```
   AMADEUS_API_KEY=YOUR_API_KEY
   AMADEUS_API_SECRET=YOUR_API_SECRET
   ```

## Usage

### 1. Adding a Flight Alert

```bash
PYTHONPATH=flight_tracker python3 flight_tracker/cli.py <ORIGIN_CITY/IATA> <DESTINATION_CITY/IATA> <TARGET_PRICE> [DEPARTURE_DATE (YYYY-MM-DD)]
```

### 2. Checking for Price Drops

```bash
PYTHONPATH=flight_tracker python3 flight_tracker/main.py
```
