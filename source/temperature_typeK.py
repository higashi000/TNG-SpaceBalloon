#!/usr/bin/python
from max31855 import MAX31855, MAX31855Error
import RPi.GPIO as GPIO
import time 
import outputFile
import sys

cs_pin = 24
clock_pin = 23
data_pin = 21
units = "c"

args = sys.argv

output = outputFile.OutputFile('temperature_K_')

thermocouple = MAX31855(cs_pin, clock_pin, data_pin, units, GPIO.BOARD)
output.output_file(args[1], thermocouple.get())
thermocouple.cleanup()
