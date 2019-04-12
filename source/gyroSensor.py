import smbus
import time
import outputFile
import sys

bus = smbus.SMBus(1)

bus.write_byte_data(0x6A, 0x20, 0x0F)
bus.write_byte_data(0x6A, 0x23, 0x30)

time.sleep(0.5)

data0 = bus.read_byte_data(0x6A, 0x28)
data1 = bus.read_byte_data(0x6A, 0x29)

xGyro = data1 * 256 + data0
if xGyro > 32767 :
	xGyro -= 65536

data0 = bus.read_byte_data(0x6A, 0x2A)
data1 = bus.read_byte_data(0x6A, 0x2B)

yGyro = data1 * 256 + data0
if yGyro > 32767 :
	yGyro -= 65536

data0 = bus.read_byte_data(0x6A, 0x2C)
data1 = bus.read_byte_data(0x6A, 0x2D)


zGyro = data1 * 256 + data0
if zGyro > 32767 :
	zGyro -= 65536

args = sys.argv

output = outputFile.OutputFile('gyro')
outputValue = str(xGyro) + ',' + str(yGyro) + ',' + str(zGyro)

output.output_file(args[1], outputValue)



