from datetime import datetime

from app.core.utils import TZ
from app.core.db import DBConnection

db = DBConnection()


def insert_climate(temp, hum):
    time = datetime.now(TZ)
    db.write_query(
        "INSERT INTO climate (time, temperature, humidity) VALUES (%s, %s, %s)",
        (time, temp, hum),
    )


def insert_moisture(status):
    time = datetime.now(TZ)
    db.write_query(
        "INSERT INTO moisture (time, status) VALUES (%s, %s)",
        (time, status),
    )
