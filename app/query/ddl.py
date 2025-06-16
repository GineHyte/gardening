from app.core.db import DBConnection
from app.core.logger import logger

db = DBConnection()


def create_climat_table():
    db.write_query(
        """
            CREATE TABLE IF NOT EXISTS climate (
                time TIMESTAMP,
                temperature FLOAT,
                humidity FLOAT
            )
        """
    )
    logger.info("Climate table created or already exists.")


def create_moisture_table():
    db.write_query('CREATE TABLE IF NOT EXISTS moisture (time TIMESTAMP, status INT)')
    logger.info("Moisture table created or already exists.")

def drop_climate_table():
    db.write_query("DROP TABLE IF EXISTS climate")
    logger.info("Climate table dropped if it existed.")

def drop_moisture_table():
    db.write_query("DROP TABLE IF EXISTS moisture")
    logger.info("Moisture table dropped if it existed.")