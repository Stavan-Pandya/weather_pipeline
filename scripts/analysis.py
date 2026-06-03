import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("sqlite:///database/weather.db")

# SQL Query
query = """
SELECT city, AVG(temperature) as avg_temp
FROM weather
GROUP BY city
"""

df = pd.read_sql(query, engine)

print("\nAverage Temperature Data")
print(df)

# Chart
df.plot(
    x="city",
    y="avg_temp",
    kind="bar"
)

plt.title("Average Temperature by City")
plt.ylabel("Temperature °C")

plt.savefig("output/weather_chart.png")

plt.show()