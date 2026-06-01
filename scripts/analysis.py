import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("sqlite:///database/weather.db")

query = "SELECT * FROM weather"

df = pd.read_sql(query, engine)

print(df)

df.plot(
    x="city",
    y="temperature",
    kind="bar"
)

plt.title("City Temperature")
plt.ylabel("Temperature °C")

plt.savefig("output/weather_chart.png")

plt.show()