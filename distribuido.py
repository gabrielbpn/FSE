import socket, sys
import new

HOST = sys.argv[-1]

PORT = 10481

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dest = (HOST, PORT)

tcp.connect(dest)

msg = input()

while True:

	tcp.send(str(msg).encode())
	
	msg = input()
	menu(msg)

	
	




tcp.close()

# ssh gabriel@164.41.98.28 -p 13508
