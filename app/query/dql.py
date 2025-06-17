from app.core.db import DBConnection

db = DBConnection()

def get_last_moisture():
    query = "SELECT time, status FROM moisture ORDER BY time DESC LIMIT 1"
    result = db.read_query(query)
    if result:
        return result[0][1]
    return None