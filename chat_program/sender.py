#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Enter the message : ")
while True:
	s_message = input("Sender  :      ")
	s.sendto(s_message.encode(),("192.168.10.47",9988))
	data = s.recvfrom(1000)
	print(data[0].decode())
