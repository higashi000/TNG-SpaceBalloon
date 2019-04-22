#!/bin/sh

_i=1
_one=1

while :
do
  _nowTime=`date "+%H%m%S"`
  _canGetTemperature=$(($_i%60))
  if [ $_canGetTemperature = 0 ]; then
    python3 ./temperature-humidity_sensor.py $_nowTime &
	python3 ./temperature_typeK.py $_nowTime &
  fi

  python3 ./acceleration_gyro_magAddress.py $_nowTime &

  _i=$(($_i + $_one))
  sync
  sleep 1
done
