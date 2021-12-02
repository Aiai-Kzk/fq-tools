#!/bin/python3

import argparse
import socket
import time

parser = argparse.ArgumentParser(description='analyze the pcap-file')

parser.add_argument('-i', '--interval', help='packet interval', type=float, default=0.001)
parser.add_argument('-l', '--len', help='packet length', type=int, default=300)
parser.add_argument('-n', '--num', help='num of Tx packet', type=int, default=1000)

# parser.add_argument('--arg3')
# parser.add_argument('-a', '--arg4') 

args = parser.parse_args()

packet_num = args.num
packet_len = args.len
interval = args.interval

raw_msg = "x" * packet_len

s_ip = "127.0.0.1"
s_port = 52001
# アドレス・ポート

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(packet_num):
    msg = str(raw_msg)
    client.sendto(msg.encode(), (s_ip, s_port))

    print("packet_number:", i)
    time.sleep(interval)
