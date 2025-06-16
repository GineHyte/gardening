import time

from app.core.logger import logger, init_logging
from app.core.db import DBConnection
from app.sensors import iter_climate, iter_moisture, init_gpio
from app.query.ddl import create_climat_table, create_moisture_table
from app.query.dml import insert_climate, insert_moisture
from app.core.config import settings

init_logging()

db = DBConnection()
if db.test():
    logger.info("Database connection established successfully.")
else:
    logger.error("Failed to connect to the database.")

def main():
    logger.info("Starting the application...")
    create_climat_table()
    create_moisture_table()
    if not settings.TEST:
        init_gpio()  # Initialize GPIO pins for sensors
    else:
        logger.warning("Running in test mode, GPIO initialization skipped.")
        logger.warning("Using mock data for sensors.")
    while True:
        try:
            for data in iter_climate():
                if "error" in data:
                    logger.error(data["error"])
                else:
                    insert_climate(data["temperature"], data["humidity"])
                    logger.info(f"Inserted climate data: {data}")

            for data in iter_moisture():
                insert_moisture(data["status"])
                logger.info(f"Inserted moisture data: {data}")

            time.sleep(settings.TIMEOUT)  # Adjust the sleep time as needed
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            time.sleep(settings.TIMEOUT)  


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Application stopped by user.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        db.close()
        logger.info("Database connection closed.")