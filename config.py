DB_USER = "postgres"

DB_PASSWORD = "virat"

DB_HOST = "localhost"

DB_PORT = "5432"

DB_NAME = "weather_db"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)