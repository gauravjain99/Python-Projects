#!/usr/bin/python3

import socket
import threading 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_address = socket.gethostbyname(socket.gethostname())
port = 9998

# IP address of the person to talk to 
opposite_ip = input("Enter IP address of the person to talk to : ")

s.bind((ip_address,port))

print("Enter the message : ")

def send_func():
	while True:
		s_message = input()
		s.sendto(("Sender : " + s_message).encode(),(opposite_ip,9988))
	
def recv_func():
	while True:
		data = s.recvfrom(1000)
		print(data[0].decode())

threading._start_new_thread(send_func,())
threading._start_new_thread(recv_func, ())

while True:
	pass 
