import serial
import micropyGPS
import threading
import time
import outputFile
import sys
from time import sleep

gps = micropyGPS.MicropyGPS(9, 'dd') # MicroGPSオブジェクトを生成する。
                                     # 引数はタイムゾーンの時差と出力フォーマット

def rungps(): # GPSモジュールを読み、GPSオブジェクトを更新する
    s = serial.Serial('/dev/serial0', 9600, timeout=10)
    s.readline() # 最初の1行は中途半端なデーターが読めることがあるので、捨てる
    while True:
        sentence = s.readline().decode('utf-8') # GPSデーターを読み、文字列に変換する
        if sentence[0] != '$': # 先頭が'$'でなければ捨てる
            continue
        for x in sentence: # 読んだ文字列を解析してGPSオブジェクトにデーターを追加、更新する
            gps.update(x)

gpsthread = threading.Thread(target=rungps, args=()) # 上の関数を実行するスレッドを生成
gpsthread.daemon = True
gpsthread.start() # スレッドを起動

args = sys.argv

latitudeOutput = outputFile.OutputFile('gps_latitude')
longitudeOutput = outputFile.OutputFile('gps_longitude')
aboveSeaLevelOutput = outputFile.OutputFile('gps_aboveSeaLevel')
now_time = args[1]
hand_over_time = now_time.replace('/', '')

latitudeOutput.output_file(hand_over_time, gps.latitude[0])
longitudeOutput.output_file(hand_over_time, gps.longitude[0])
aboveSeaLevelOutput.output_file(hand_over_time, gps.altitude)
