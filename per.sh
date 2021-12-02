#!/bin/bash

dir=$1
echo $dir

cd $dir

trap exit SIGINT

if [ "$dir" = "fq" ]
then
  for i in {0..7}
  do
    ./wifi_pcap.py wifi-fq-mcs$i.pcap
    
  done
elif [ $dir = "dr" ]
then
  for i in {0..7}
  do
    ./wifi_pcap.py wifi-mcs$i.pcap
  done
else
  echo "Error!!"
fi
