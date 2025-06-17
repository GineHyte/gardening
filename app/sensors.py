import time

from app.core.config import settings
from app.query.dql import get_last_moisture
from app.core.logger import logger

if not settings.TEST:
    import Adafruit_DHT
    import RPi.GPIO as GPIO
else:
    import random

def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(settings.MOISTURE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setmode(GPIO.BCM) 
    GPIO.setwarnings(False) 
    GPIO.setup(settings.BUZZER_PIN, GPIO.OUT)


#last_temp = None
#last_hum = None
#last_status = 0


def iter_climate():
    global last_temp, last_hum
    if not settings.TEST:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, settings.CLIMATE_PIN)
    else:
        humidity = random.uniform(30.0, 70.0)  # Mock humidity data
        temperature = random.uniform(20.0, 30.0)
    if humidity is not None and temperature is not None:
        #temp = round(temperature, 1)
        #hum = round(humidity, 1)
       # if last_temp == temp or last_hum == hum:
            #return
        #last_temp = temp
        #last_hum = hum
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
    #last_status = moisture_status
    if moisture_status == 1:
        make_some_noise()
    yield {"status": moisture_status}


def make_some_noise():
    if settings.TEST:
        logger.info("Test mode: Simulating buzzer sound.")
    else:
        for _ in range(2): 
            pwm = GPIO.PWM(settings.BUZZER_PIN, 2000) 
            pwm.start(50) 
            time.sleep(0.2) 
            pwm.stop() 
            GPIO.cleanup(settings.BUZZER_PIN)  
            GPIO.setup(settings.BUZZER_PIN, GPIO.OUT)  
            time.sleep(0.2)