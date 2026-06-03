import requests
import pandas as pd
from datetime import datetime

API_KEY = "5c85ec4bdd47143148371e8fd1f03a1c"

cities = [
    "Bangalore",
    "Delhi",
    "Mumbai",
    "Ahmedabad",
    "Chennai"
]

all_weather_data = []

for CITY in cities:

    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    print(f"\nWeather Data for {CITY}")
    print(data)

    # Error handling
    if "main" not in data:
        print(f"API Error for {CITY}: {data}")
        continue

    weather_data = {
        "city": CITY,
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather": data["weather"][0]["main"],
        "wind_speed": data["wind"]["speed"],
        "clouds": data["clouds"]["all"],
        "visibility": data.get("visibility", 0),
        "timestamp": datetime.now()
    }

    all_weather_data.append(weather_data)

df = pd.DataFrame(all_weather_data)

df.to_csv("data/weather_raw.csv", index=False)

print("\nWeather data extracted successfully!")
print(df)