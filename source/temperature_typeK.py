#!/usr/bin/python
from max31855 import MAX31855, MAX31855Error
import RPi.GPIO as GPIO
import time 

cs_pin = 24
clock_pin = 23
data_pin = 21
units = "c"

while 1:
	thermocouple = MAX31855(cs_pin, clock_pin, data_pin, units, GPIO.BOARD)
	print(thermocouple.get())
	thermocouple.cleanup()
	time.sleep(1)
