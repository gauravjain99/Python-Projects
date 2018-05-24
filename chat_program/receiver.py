#!/usr/bin/python3

import socket
import time 
import threading


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_address = socket.gethostbyname(socket.gethostname())
port = 9988
  
opposite_ip = input("Enter IP address of the perosn to talk to : ")

s.bind((ip_address,port))


def recv_func():
	while True:
		data = s.recvfrom(1000)
		#print(data)
		print(data[0].decode())
	
def send_func():
	while True:
		message  = input()
		encoded_message = ("Receiver : " + message).encode()
		#sender_address = data[1]	
		#print(data[1])
		s.sendto(encoded_message,(opposite_ip,9998))


threading._start_new_thread(recv_func, ())
threading._start_new_thread(send_func, ())


# to make the threads run 
while True:
	pass		
