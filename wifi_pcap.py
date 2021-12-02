#!/usr/bin/python3

import pyshark
import argparse
import numpy as np

TX_PACKET = 10000

parser = argparse.ArgumentParser(description='analyze the pcap-file')

parser.add_argument('pcap_file', help='name of the pcap-file')
# parser.add_argument('arg2', help='foooo')
# parser.add_argument('--arg3')
# parser.add_argument('-a', '--arg4') 

args = parser.parse_args()

cap = pyshark.FileCapture(args.pcap_file)

snr = []
num = 0

for p in cap:
    try:
        #print(p)
        snr.append(10 ** (int(p.wlan_radio.signal_dbm) / 10))
        num += 1
    except AttributeError as e:
        continue

snr = np.array(snr)

#print("Average_SNR,", 10 * np.log10(np.average(snr)))
print(1 - num / TX_PACKET)
