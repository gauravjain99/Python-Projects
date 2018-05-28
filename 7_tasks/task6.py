import socket
import subprocess

ip_address = socket.gethostbyname(socket.gethostname())
ip_range = ip_address+'/24'
#print(ip_range)
ip = subprocess.getoutput('nmap -sn -n ' + ip_range + ' > iptest.txt')
#print(ip)

addresses = list()

fhand = open('iptest.txt', 'r')

for line in fhand:
#	print(line)
	line = line.strip()
	if line.startswith("Nmap scan report for"):
		addresses.append(line)		

for ip in addresses:
	ip_number = ip.split()
	final = ip_number[-1]
	print(final)
#print(addresses)

subprocess.getoutput('rm -f iptest.txt')
