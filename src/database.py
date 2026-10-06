import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("POSTGRES_PASSWORD")

connection = psycopg.connect(
    f"host=localhost port=5432 user=ticketiq_app dbname=ticketiq_db password={password}"
)

print("Successfully connected to PostgreSQL")