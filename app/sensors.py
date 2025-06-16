from app.core.config import settings

if not settings.TEST:
    import Adafruit_DHT
    import RPi.GPIO as GPIO
else:
    import random

def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


last_temp = None
last_hum = None
#last_status = 0


def iter_climate():
    global last_temp, last_hum
    if not settings.TEST:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
    else:
        humidity = random.uniform(30.0, 70.0)  # Mock humidity data
        temperature = random.uniform(20.0, 30.0)
    if humidity is not None and temperature is not None:
        temp = round(temperature, 1)
        hum = round(humidity, 1)
        if last_temp == temp or last_hum == hum:
            return
        last_temp = temp
        last_hum = hum
        yield {"temperature": temperature, "humidity": humidity}
    else:
        yield {"error": "Failed to retrieve data from the sensor"}


def iter_moisture():
    #global last_status
    if not settings.TEST:
        moisture_status = GPIO.input(22)
    else:
        moisture_status = random.choice([0, 1])
    #if moisture_status == last_status:
        #return
    last_status = moisture_status
    yield {"status": moisture_status}
