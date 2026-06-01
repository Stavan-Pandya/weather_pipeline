import pandas as pd

df = pd.read_csv("data/weather_raw.csv")

df["temperature_fahrenheit"] = (df["temperature"] * 9/5) + 32

df["humidity_category"] = df["humidity"].apply(
    lambda x: "High" if x > 70 else "Normal"
)

df.to_csv("data/weather_transformed.csv", index=False)

print("Data transformed successfully!")
print(df)