import requests
import pandas as pd
from datetime import datetime

API_KEY = "5c85ec4bdd47143148371e8fd1f03a1c"
CITY = "Bangalore"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(data)

if "main" not in data:
    print("API Error:", data)
    exit()

weather_data = {
    "city": CITY,
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "pressure": data["main"]["pressure"],
    "weather": data["weather"][0]["main"],
    "wind_speed": data["wind"]["speed"],
    "timestamp": datetime.now()
}

df = pd.DataFrame([weather_data])

df.to_csv("data/weather_raw.csv", index=False)

print("Weather data extracted successfully!")
print(df)