import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data/weather_transformed.csv")

engine = create_engine("sqlite:///database/weather.db")

# Historical loading
df.to_sql(
    "weather",
    engine,
    if_exists="append",
    index=False
)

print("\nData loaded into SQLite database!")