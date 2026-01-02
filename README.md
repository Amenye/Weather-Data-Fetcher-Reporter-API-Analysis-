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

Connecting to London....✅ Done.
Connecting to Chicago....✅ Done.
Connecting to Pretoria....✅ Done.
Connecting to Johannesburg....✅ Done.
Connecting to Tokyo....✅ Done.

--- COLLECTION COMPLETE ---
Successfully collected: 5 records.
Preview of first record: {'city': 'London', 'temp': 6.17, 'humidity': 83, 'description': 'clear sky', 'timestamp': datetime.datetime(2025, 12, 27, 12, 55, 4)}

---THE RAW TABLE---
           city   temp  humidity      description           timestamp
0        London   6.17        83        clear sky 2025-12-27 12:55:04
1       Chicago   3.74        90  overcast clouds 2025-12-27 12:51:59
2      Pretoria  26.06        61       few clouds 2025-12-27 12:51:31
3  Johannesburg  25.90        70       few clouds 2025-12-27 12:51:36
4         Tokyo   4.63        57       few clouds 2025-12-27 12:50:21

✅ Data appended to weather_log.csv

---ANALYSIS REPORT---
Cities Queried: 5
Average Humididty: 72.2%
Hottest City: Pretoria (26.06°C)
Coldest City: Chicago (3.74°C)
```
## ⚙️ How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Amenye/weather-etl-pipeline.git](https://github.com/Amenye/weather-etl-pipeline.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install pandas requests
    ```
3.  **Configure API Key:**
    * Open `weather_etl_pipeline.py`
    * Replace `"INSERT_YOUR_API_KEY_HERE"` with your valid OpenWeatherMap key.
    *(Note: For production environments, use environment variables).*
4.  **Execute the script:**
    ```bash
    python weather_etl_pipeline.py
    ```

## 📈 Future Improvements
* **Visualization:** Integrate `Matplotlib` to generate trend lines for temperature changes over the last 7 days.
* **Automation:** Set up a cron job (Linux) or Task Scheduler (Windows) to run the script automatically every 24 hours.
* **Cloud Storage:** Upgrade the "Load" phase to save data to an AWS S3 bucket or a SQL database instead of a local CSV.
