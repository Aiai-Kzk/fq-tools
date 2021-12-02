#!/bin/sh

for i in {1..8}
do
	num=$(($i - 1))
       	mv wifi_mcs$i.pcap wifi-mcs$num.pcap
done
