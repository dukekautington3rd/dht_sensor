import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 22)

while True:
    result = instance.read()
    if result.is_valid():
        print(f"Temp:    {result.temperature * 1.8 + 32}F")
        print(f"Hum:       {result.humidity}%")
    time.sleep(10)