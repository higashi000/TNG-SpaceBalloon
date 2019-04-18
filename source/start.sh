#!/bin/sh

_i=1
_one=1

while :
do
  echo aaaaaaaaaaaaaaaaaaaaaaaaaa
  _nowTime=`date "+%H%m%S"`
  _canGetTemperature=$(($_i%60))
  if [ $_canGetTemperature = 0 ]; then
    echo gregreuophfgesioh@gioh@ugreuophgreauopbagrewio
    python3 ./temperature-humidity_sensor.py $_nowTime &
  fi

  _i=$(($_i + $_one))
  sync
  sleep 1
done
