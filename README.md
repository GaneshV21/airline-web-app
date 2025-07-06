# Airline Booking Market Demand Web App

## Overview

This web application fetches, processes, and visualizes airline booking market demand data. The app aims to provide actionable insights such as popular flight routes, top airlines, and flight status distributions to help understand current airline booking trends.

---

## Features

- **Data Fetching:** Loads airline flight data from a local JSON file (or API) for analysis.
- **Data Processing:** Cleans and aggregates data to identify popular routes, top airlines, and flight status distributions.
- **Visualization:** Presents data visually using interactive charts powered by Chart.js.
- **User Interface:** Simple and intuitive web interface for easy data exploration.

---

## Project Structure

- `app.py` - Main Flask application script.
- `templates/index.html` - Frontend template with charts and tables.
- `flights.json` - Sample flight data used for processing and visualization.

---


## How to Run

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt