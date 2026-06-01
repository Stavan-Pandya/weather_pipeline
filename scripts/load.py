import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data/weather_transformed.csv")

engine = create_engine("sqlite:///database/weather.db")

df.to_sql("weather", engine, if_exists="replace", index=False)

print("Data loaded into SQLite database!")