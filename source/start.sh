#!/bin/sh

_i=0
_one=1
_getGPSTime=0

cd ../outputData
_temperature_typeK_cnt=$(($(ls -1 | grep 'temperature_K' | sed -e "s/temperature_K_//g" -e "s/.txt//g" | sort -n | tail -n 1) + $_one))
_gps_cnt=$(($(ls -1 | grep 'gps_latitude' | sed -e "s/gps_latitude//g" -e "s/.txt//g" | sort -n | tail -n 1) + $_one))
_temperaturehumidity_cnt=$(($(ls -1 | grep 'temperature' | sed -e "s/temperature//g" -e "s/.txt//g" | sort -n | tail -n 1) + $_one))
_acceleration_gyro_magAddress_cnt=$(($(ls -1 | grep 'acceleration' | sed -e "s/acceleration//g" -e "s/.txt//g" | sort -n | tail -n 1) + $_one))
cd ../source

while :
do
  _canGetTemperature=$(($_i%60))
  _canGPS=$(($_i%10))
  _nowTime=`date "+%H%M%S"`
  if [ $_canGetTemperature = 0 ]; then
    python3 ./temperature_typeK.py $_temperature_humidity_cnt $_getGPSTime &
    python3 ./temperature-humidity_sensor.py $_temperature_humidity_cnt $_getGPSTime &
    _temperature_humidity_cnt=$(($_temperature_humidity_cnt + $_one))
    _temperature_typeK_cnt=$(($_temperature_typeK_cnt + $_one))
  fi

  if [ $_canGPS = 0 ]; then
    python3 ./gps.py $_gps_cnt $_getGPSTime &
    _gps_cnt=$(($_gps_cnt + $_one))
    echo $_gps_cnt
  fi

  python3 ./acceleration_gyro_magAddress.py $_acceleration_gyro_magAddress_cnt $_getGPSTime &
  _acceleration_gyro_magAddress_cnt=$(($_acceleration_gyro_magAddress_cnt + $_one))

  _i=$(($_i + $_one))
  sync
  sleep 1
done
