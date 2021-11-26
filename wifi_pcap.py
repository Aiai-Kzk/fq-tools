#!/bin/python3

import pyshark
import argparse

TX_PACKET = 1000

parser = argparse.ArgumentParser(description='analyze the pcap-file')

parser.add_argument('pcap_file', help='name of the pcap-file')
# parser.add_argument('arg2', help='foooo')
# parser.add_argument('--arg3')
# parser.add_argument('-a', '--arg4') 

args = parser.parse_args()

cap = pyshark.FileCapture(args.pcap_file)

snr = []

for p in cap:
    try:
        snr.append(int(p.wlan_radio.snr))
        
    except AttributeError as e:
        continue

snr = np.array(snr)

print("Average_SNR," np.averange(snr))
print("PER,", len(cap) / TX_PACKET)
