#!/bin/sh

_i=0
_one=1

while :
do
   _canGetTemperature=$(($_i%60))
   _nowTime=`date "+%H%m%S"`
#  if [ $_canGetTemperature = 0 ]; then
    python3 ./temperature_typeK.py $_nowTime &
#  fi

#  python3 ./acceleration_gyro_magAddress.py $_nowTime &

  _i=$(($_i + $_one))
  sync
  sleep 1
done
