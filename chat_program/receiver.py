#!/usr/bin/python3

import socket
import time 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_address = socket.gethostbyname(socket.gethostname())
port = 9988

s.bind((ip_address,port))

while True:
	data = s.recvfrom(1000)
	print(data[0].decode())

	message  = input("Reveiver :     ")
	encoded_message = message.encode()
	
	s.sendto(encoded_message,(data[1][0],data[1][1]))

		
