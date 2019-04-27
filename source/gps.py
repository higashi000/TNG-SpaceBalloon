import serial
import micropyGPS
import threading
import time
import outputFile
import sys

gps = micropyGPS.MicropyGPS(9, 'dd')

def rungps():
    s = serial.Serial('/dev/serial0', 9600, timeout=10)
    s.readline()
    while True:
        sentence = s.readline().decode('utf-8')
        if sentence[0] != '$':
            continue
        for x in sentence:
            gps.update(x)

gpsthread = threading.Thread(target=rungps, args=())
gpsthread.daemon = True
gpsthread.start()

args = sys.argv

latitudeOutput = outputFile.OutputFile('gps_latitude')
longitudeOutput = outputFile.OutputFile('gps_longitude')
aboveSeaLevelOutput = outputFile.OutputFile('gps_aboveSeaLevel')
now_time = args[1]
hand_over_time = now_time.replace('/', '')

if gps.clean_sentences > 20:
    gps_latitude = str(gps.latitude[0])
    gps_longitude = str(gps.longitude[0])
    gps_seaLevel = str(gps.altitude)
    h = gps.timestamp[0] if gps.timestamp[0] < 24 else gps.timestamp[0] - 24
    latitudeOutput.output_file(hand_over_time, gps_latitude[0:8])
    longitudeOutput.output_file(hand_over_time, gps_longitude[0:8])
    aboveSeaLevelOutput.output_file(hand_over_time, gps_seaLevel[0:8])
