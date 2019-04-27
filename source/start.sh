#!/bin/sh

_i=0
_one=1

while :
do
  _canGetTemperature=$(($_i%60))
  _canGPS=$(($_i%10))
  _nowTime=`date "+%H%M%S"`
  echo $_nowTime
  if [ $_canGetTemperature = 0 ]; then
    echo "temperature_typeK"
    python3 ./temperature_typeK.py $_nowTime &
    echo "temperature humidity"
    python3 ./temperature-humidity_sensor.py $_nowTime &
  fi

  if [ $_canGPS = 0 ]; then
    echo "gps"
    python3 ./gps.py $_nowTime &
  fi

  echo "9_1"
  python3 ./acceleration_gyro_magAddress.py $_nowTime &
  echo "9_2"
  python3 ./acceleration_gyro_magAddress2.py $_nowTime &

  _i=$(($_i + $_one))
  sync
  sleep 1
done
