import time
import smbus
import sys
import outputFile
from time import sleep

def tempChanger(msb, lsb):
    mlsb = ((msb << 8) | lsb)                                             # P1
    return (-45 + 175 * int(str(mlsb), 10) / (pow(2, 16) - 1))            # P2

def humidChanger(msb, lsb):
    mlsb = ((msb << 8) | lsb)
    return (100 * int(str(mlsb), 10) / (pow(2, 16) - 1))


def getTemp():
    i2c = smbus.SMBus(1)
    i2c_addr = 0x45
    i2c.write_byte_data(i2c_addr, 0x21, 0x30)
    sleep(0.5)
    i2c.write_byte_data(i2c_addr, 0xE0, 0x00)
    data = i2c.read_i2c_block_data(i2c_addr, 0x00, 6)
    return str('{:.4g}'.format(tempChanger(data[0], data[1])))

def getHumid():
    i2c = smbus.SMBus(1)
    i2c_addr = 0x45
    i2c.write_byte_data(i2c_addr, 0x21, 0x30)
    sleep(0.5)
    i2c.write_byte_data(i2c_addr, 0xE0, 0x00)
    data = i2c.read_i2c_block_data(i2c_addr, 0x00, 6)
    return str('{:.4g}'.format(humidChanger(data[3], data[4])))

args = sys.argv

try:
    tempOutput = outputFile.OutputFile('temperature')
    outputTempValue = getTemp()
    tempOutput.output_file(args[2], args[1], outputTempValue)
    humidOutput = outputFile.OutputFile('humidity')
    outputHumidValue = getHumid()
    humidOutput.output_file(args[2], args[1], outputHumidValue)
    sleep(1)

except KeyboardInterrupt:
    pass 
