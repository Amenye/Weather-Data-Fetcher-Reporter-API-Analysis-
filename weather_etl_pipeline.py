# %%
#FINAL PROGRAM
#WEATHER DATA FETCHER & REPORTER(API + ANALYSIS)

#Importing all necessary libraries
from urllib import request
import pandas as pd
import numpy as np
import bs4 as Beautifulsoup
import requests
from datetime import datetime
import time
import os

#Declaring OpenWeatherMap API URL
weather_url = "https://api.openweathermap.org/data/2.5/weather"

#Declaring my API key
api_key = "INSERT_YOUR_API_KEY_HERE"

#Declaring the list of coutries
lst_city = ['London', 'Chicago', 'Pretoria', 'Johannesburg', 'Tokyo']
#Empty list of all the collected data
all_weather_data = []

print(f"Starting data collection for {len(lst_city)} cities...\n")
for city in lst_city:
    #Constructing request URL
    request_url = f"{weather_url}?q={city}&appid={api_key}&units=metric"

    try:
        #Retrieving the data
        response = requests.get(request_url)

        #Checking the status of the request
        if response.status_code == 200:

            print(f"Connecting to {city}....✅ Done.")

            #Parsing the data
            data = response.json()

            #1. Accesing the city name
            city_name = data['name']

            #2. Accesing the temperature
            temp = data['main']['temp']

            #3. Accessing the humidity
            humidity = data['main']['humidity']

            #4. Accesing date
            timestamp = data['dt']
            readable_date = datetime.fromtimestamp(timestamp)

            #5. Accesing weather discription
            weather_desc = data['weather'][0]['description']

            #Dictionary of a city record
            city_record = {'city': city_name,'temp': temp, 'humidity': humidity, 'description': weather_desc, 'timestamp': readable_date}

            #Appending the weather data list
            all_weather_data.append(city_record)
        else:
            print("There was an error. The server rejected us.")
            print(f"Status code: {response.status_code}")

    except Exception as e:
        print(f"⚠️ Error: {e}")

    time.sleep(1)

# --- THE OUTPUT ---
print("\n--- COLLECTION COMPLETE ---")
print(f"Successfully collected: {len(all_weather_data)} records.")
print("Preview of first record:", all_weather_data[0])

#Creating a data frame of all the weather data
df = pd.DataFrame(all_weather_data)
print('\n---THE RAW TABLE---')
print(df)

#ANALYSIS OF THE WEATHER DATA
#1. Average Humidity
avg_humidity = df['humidity'].mean()

#2. Hottest City
hottest_index = df['temp'].idxmax() #Index of the hottest city
hottest_city = df.loc[hottest_index]

#3. Coldest City
coldest_index = df['temp'].idxmin()
coldest_city = df.loc[coldest_index]


##Saving the information to a csv file
#Configuring the file name
file_name = 'weather_log.csv'

#Checking if the file exists
file_exists = os.path.isfile(file_name)

#Writing the data to the csv file
df.to_csv(file_name, mode = 'a', header = not file_exists, index = False)

print(f"\n✅ Data appended to {file_name}")

#---THE FINAL REPORT---
print('\n---ANALYSIS REPORT---')
print(f'Cities Queried: {len(df)}')
print(f'Average Humididty: {avg_humidity}%')

print(f"Hottest City: {hottest_city['city']} ({hottest_city['temp']}°C)")
print(f"Coldest City: {coldest_city['city']} ({coldest_city['temp']}°C)")


# %%
