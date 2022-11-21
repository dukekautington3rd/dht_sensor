import board
import adafruit_shtc3
import time


# initialize GPIO
i2c = board.I2C()

# read data using pin
sht = adafruit_shtc3.SHTC3(i2c)


while True:
    temperature, relative_humidity = sht.measurements
    print(time.ctime())
    print(f"Temperature: {temperature * 1.8 + 32}F")
    print(f"Humidity: {relative_humidity}%")
    print("")
    time.sleep(60)
