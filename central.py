import socket, sys

HOST = sys.argv[-1]

PORT = 10671

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ori = (HOST, PORT)

tcp.bind(ori)

tcp.listen(1)

print('Servidor TCP Iniciado no IP', HOST, 'na porta', PORT)

while True:
	conexao, cliente = tcp.accept()

	print('Cliente entrou:', cliente)

	while True:
		mensagem = conexao.recv(1024)

		print('\nCLiente...:', cliente)
		print('Mensagem:', mensagem.decode())

	print('Finalizando a conexao do cliente: ', cliente)
	conexao.close()
