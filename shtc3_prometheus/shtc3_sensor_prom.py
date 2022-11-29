from prometheus_client import start_http_server, Gauge
from os import environ
import board
import adafruit_shtc3
import time


if not "room" in environ:
    room = 'No Room'
else:
    room = environ.get('room')


# initialize GPIO
i2c = board.I2C()

# read data using pin
sht = adafruit_shtc3.SHTC3(i2c)

# defined gauges to track 
env_temp = Gauge('env_temp', 'Temperature ', ['room'])
env_hum = Gauge('env_hum', 'Humidity', ['room'])

start_http_server(8188)
while True:
    temperature, relative_humidity = sht.measurements
    ftemperature = temperature * 1.8 + 32
    
    env_temp.labels(room=room).set(ftemperature)
    env_hum.labels(room=room).set(relative_humidity)

    time.sleep(60)
