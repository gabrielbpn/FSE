import socket, sys

HOST = sys.argv[-1]

PORT = 10481

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ori = (HOST, PORT)

tcp.bind(ori)

tcp.listen(1)

print('Servidor TCP Iniciado no IP', HOST, 'na porta', PORT)

while True:
	conexao, cliente = tcp.accept()
	print('Cliente entrou:', cliente)
	conexao2, cliente2 = tcp.accept()
	while True:
		
		mensagem = conexao.recv(1024)
		
		if not mensagem:
			break

		print('\nCLiente...:', cliente)
		print('Mensagem:', mensagem.decode())
		
		if mensagem == '0':
			liga_led.led01
	
	print('Finalizando a conexao dos clientes: ', cliente, cliente2)
	conexao.close()
