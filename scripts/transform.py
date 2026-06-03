import pandas as pd

df = pd.read_csv("data/weather_raw.csv")

# Fahrenheit conversion
df["temperature_fahrenheit"] = (df["temperature"] * 9/5) + 32

# Humidity category
df["humidity_category"] = df["humidity"].apply(
    lambda x: "High" if x > 70 else "Normal"
)

# Temperature category
df["temperature_category"] = df["temperature"].apply(
    lambda x: "Hot" if x > 30 else "Cool"
)

# Wind category
df["wind_category"] = df["wind_speed"].apply(
    lambda x: "Windy" if x > 5 else "Calm"
)

# Visibility category
df["visibility_category"] = df["visibility"].apply(
    lambda x: "Low" if x < 5000 else "Clear"
)

df.to_csv("data/weather_transformed.csv", index=False)

print("\nData transformed successfully!")
print(df)