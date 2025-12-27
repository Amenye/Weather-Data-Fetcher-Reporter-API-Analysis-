# 🌦️ Automated Weather ETL Pipeline

## 📋 Project Overview
This project is an automated Data Engineering pipeline designed to capture real-time weather data. It interfaces with the **OpenWeatherMap API** to fetch live meteorological data for a specific set of global cities, cleanses the JSON response, and aggregates the data into a persistent CSV log for historical tracking.

The system performs a full **ETL (Extract, Transform, Load)** process, allowing for the accumulation of a proprietary weather dataset over time.

## 🚀 Key Features
* **API Integration:** Handles HTTP requests and authenticates with OpenWeatherMap using custom API keys.
* **Data Transformation:** Parses complex, nested JSON objects to extract relevant metrics (Temperature, Humidity, Weather Conditions).
* **Automated Analytics:** Uses **Pandas** to instantly calculate statistics like the hottest city, coldest city, and average humidity across the dataset.
* **Persistent Logging:** Implements an "Append-Only" storage strategy to build a historical `weather_log.csv` database without overwriting previous entries.
* **Error Handling:** Includes robust `try-except` blocks to manage network failures or invalid city queries gracefully.

## 🛠️ Tech Stack
* **Python 3.10+**
* **Requests** (HTTP Protocol)
* **Pandas** (Data Manipulation & Analysis)
* **OpenWeatherMap API** (Data Source)
* **Datetime** (Temporal Data Processing)

## 📊 Sample Output
When the pipeline runs, it provides an immediate console report and updates the CSV log.

**Console Report:**
```text
Starting data collection for 5 cities...
Fetching London... ✅ Done.
Fetching New York... ✅ Done.
Fetching Tokyo... ✅ Done.
Fetching Sydney... ✅ Done.
Fetching Paris... ✅ Done.

Weather Fetch Summary - 2023-10-27
----------------------------------
Cities Queried: 5
Hottest City:   Sydney (28.4°C)
Coldest City:   London (12.1°C)
Average Humidity: 65.4%
----------------------------------
✅ Data appended to weather_log.csv
