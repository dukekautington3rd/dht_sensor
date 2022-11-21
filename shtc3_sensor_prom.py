from prometheus_client import start_http_server, Gauge
import board
import adafruit_shtc3
import time

room = 'Master Bedroom'
# initialize GPIO
i2c = board.I2C()

# read data using pin
sht = adafruit_shtc3.SHTC3(i2c)

# defined gauges to track 
env_mbr_temp = Gauge('env_mbr_temp', 'Temperature ', ['room'])
env_mbr_hum = Gauge('env_mbr_hum', 'Humidity', ['room'])

start_http_server(8188)
while True:
    temperature, relative_humidity = sht.measurements
    ftemperature = temperature * 1.8 + 32
    
    env_mbr_temp.labels(room=room).set(ftemperature)
    env_mbr_hum.labels(room=room).set(relative_humidity)

    time.sleep(60)
