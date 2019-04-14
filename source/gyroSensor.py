import smbus
import time
import outputFile
import sys

bus = smbus.SMBus(1)

bus.write_byte_data(0x6A, 0x20, 0x0F)
bus.write_byte_data(0x6A, 0x23, 0x30)

time.sleep(0.5)


def get_x_gyro():
    data0 = bus.read_byte_data(0x6A, 0x28)
    data1 = bus.read_byte_data(0x6A, 0x29)
    xGyro = data1 * 256 + data0
    if xGyro > 32767 :
        xGyro -= 65536

    return str(xGyro)

def get_y_gyro():
    data0 = bus.read_byte_data(0x6A, 0x2A)
    data1 = bus.read_byte_data(0x6A, 0x2B)
    yGyro = data1 * 256 + data0
    if yGyro > 32767 :
        yGyro -= 65536

    return str(yGyro)

def get_z_gyro():
    data0 = bus.read_byte_data(0x6A, 0x2C)
    data1 = bus.read_byte_data(0x6A, 0x2D)
    zGyro = data1 * 256 + data0
    if zGyro > 32767 :
        zGyro -= 65536

    return str(zGyro)

def marge_values():
    return get_x_gyro() + ',' + get_y_gyro() + ',' + get_z_gyro() + '\n'

args = sys.argv

output = outputFile.OutputFile('gyro')

i = 0.0
gyro_Value = ""
while i <= 1 :
    gyro_Value += marge_values()

    i += 0.01666666666666666666666666666666

output.output_file(args[1], gyro_Value)
