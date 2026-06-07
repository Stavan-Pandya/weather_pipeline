import pandas as pd
from sqlalchemy import create_engine
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from config import DATABASE_URL

df = pd.read_csv("data/weather_transformed.csv")

engine = create_engine(DATABASE_URL)

df.to_sql(
    "weather",
    engine,
    if_exists="append",
    index=False
)

print("Data loaded into PostgreSQL successfully!")