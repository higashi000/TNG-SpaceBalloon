import smbus
import time
import outputFile
import sys

bus = smbus.SMBus(1)


# acceleration --- {{{

def acceleration() :
    bus.write_byte_data(0x19, 0x0F, 0x03)
    bus.write_byte_data(0x19, 0x10, 0x08)
    bus.write_byte_data(0x19, 0x11, 0x00)

#   time.sleep(0.5)

    data = bus.read_i2c_block_data(0x19, 0x02, 6)

    xAccl = ((data[1] * 256) + (data[0] & 0xF0)) / 16
    if xAccl > 2047 :
        xAccl -= 4096
    yAccl = ((data[3] * 256) + (data[2] & 0xF0)) / 16
    if yAccl > 2047 :
        yAccl -= 4096
    zAccl = ((data[5] * 256) + (data[4] & 0xF0)) / 16
    if zAccl > 2047 :
        zAccl -= 4096

    return str(xAccl) + ',' + str(yAccl) + ',' + str(zAccl) + '\n'

# ---}}}

# gyro {{{

def gyro() :
    bus.write_byte_data(0x69, 0x0F, 0x04)
    bus.write_byte_data(0x69, 0x10, 0x07)
    bus.write_byte_data(0x69, 0x11, 0x00)

#   time.sleep(0.5)

    data = bus.read_i2c_block_data(0x69, 0x02, 6)

    xGyro = data[1] * 256 + data[0]
    if xGyro > 32767 :
        xGyro -= 65536
    yGyro = data[3] * 256 + data[2]
    if yGyro > 32767 :
        yGyro -= 65536
    zGyro = data[5] * 256 + data[4]
    if zGyro > 32767 :
        zGyro -= 65536

    return str(xGyro) + "," + str(yGyro) + "," + str(zGyro) + "\n"

# }}}

outputAccleration = outputFile.OutputFile('acceleration')
outputGyro = outputFile.OutputFile('gyro')

args = sys.argv

now_time = args[1]

hand_over_time = now_time.replace('/', '')

i = 0.0
acceleration_value = ""
gyro_value = ""

while i <= 1 :
    acceleration_value += acceleration()
    gyro_value += gyro()
    i += (1 / 60)

outputAccleration.output_file(hand_over_time, acceleration_value)
outputGyro.output_file(hand_over_time, gyro_value)
