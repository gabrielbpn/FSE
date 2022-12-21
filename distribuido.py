import socket, sys, threading
import new
from new import var_temperatura, doisSegundos

HOST = sys.argv[-1]
PORT = 10654

global cont_pessoas
cont_pessoas = 0

new.passHost(HOST)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dest = (HOST, PORT)

tcp.connect(dest)

def menu():
	print("Seja bem-vindo ao menu!\n")
	while 1:

		print("\n\n--- Menu ---\n\nO que voce quer fazer?")
		
		print("1 - Ligar/desligar lampada, ar condicionado e projetor")
		print("2 - Saber os estados em tempo real")

		msg = int(input())
		tcp.send(str(msg).encode())

		print (msg)
		if msg == 1:
			print("\nDigite o numero abaixo que corresponde ao que voce quer.\n\n")

			print("1 - Ligar lampada 1")
			print("2 - Desligar lampada 1\n")

			print("3 - Ligar lampada 2")
			print("4 - Desligar lampada 2\n")

			print("5 - Ligar ar condicionado")
			print("6 - Desligar ar condicionado\n")

			print("7 - Ligar projetor")
			print("8 - Desligar projetor\n")

			print("9 - Ligar alarme")
			print("10 - Desligar alarme\n")

			print("11 - Ligar todos os dispositivos")
			print("10 - Desligar todos os alarmes\n")

			msg2 = int(input())
			tcp.send(str(msg2).encode())

			new.ligaDesligaLPA(msg2)
		
		if msg == 2:
			print("\nEsses sao os estados atuais das saidas:\n\n")
			new.estadoSaidas()
			print("\nE esses sao os estados atuais das entradas (sensores):\n\n")
			new.estadosEntradas()

thread1 = threading.Thread(target=doisSegundos, args=(var_temperatura,))
thread1.start()
menu()		

tcp.close()
