import csv
import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("POSTGRES_PASSWORD")

connection = psycopg.connect(
    f"host=localhost port=5432 user=ticketiq_app dbname=ticketiq_db password={password}"
)

cursor = connection.cursor()

with open("data/tickets.csv", newline="") as file:
    reader = csv.DictReader(file)

    for ticket in reader:
        cursor.execute(
            """
            INSERT INTO tickets (id, description, category, resolution, created_at)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                int(ticket["id"]),
                ticket["description"],
                ticket["category"],
                ticket["resolution"],
                ticket["created_at"],
            ),
        )

connection.commit()

cursor.close()
connection.close()
