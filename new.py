import RPi.GPIO as GPIO
import board, adafruit_dht
from time import sleep
from variaveis import cont_pessoas

GPIO.setmode(GPIO.BCM)

saidas = [26, 19, 13, 6, 5]

entrada_janela = 9
entrada_porta = 10
entrada_contagem_entrada = 22
entrada_contagem_saida = 27
entrada_fumaca = 11
entrada_presenca = 0

var_entrada_janela = 0
var_entrada_porta = 0
var_entrada_fumaca = 0
var_entrada_presenca = 0
var_entrada_contagem_entrada = 0
var_entrada_contagem_saida = 0

var_temperatura = adafruit_dht.DHT22(board.D18, use_pulseio=False)

saida_estados = [0,0,0,0,0]

def passHost(host):
	if ((host[-1] == "6" and host[-2] == "1") or (host[-1] == 8)):
		saidas = [18, 23, 24, 25, 8]
		entrada_janela = 12
		entrada_porta = 16
		entrada_contagem_entrada = 20
		entrada_contagem_saida = 21
		entrada_fumaca = 1
		entrada_presenca = 7

def sensorEntradaPessoa(GPIO_IN):
	global cont_pessoas 
	cont_pessoas += 1

def sensorSaidaPessoa(GPIO_IN):
	global cont_pessoas 
	cont_pessoas = max(cont_pessoas - 1, 0)

def sistemaAlarme():
	GPIO.output(saidas[4], GPIO.HIGH)

def doisSegundos(var_temperatura):
	while 1:
		sleep(6)
		temperatura(var_temperatura)

def temperatura(var_temperatura):
	try:
		temperatura_x = var_temperatura.temperature

		humildade = var_temperatura.humidity

		print("// --- \\")
		print("Temperatura: ", temperatura_x)
		print("Umidade: ", humildade)
		print("")

	except RuntimeError as error:
		pass

def sensorPresenca(channel):
	global var_entrada_presenca
	if var_entrada_presenca == 0:
		print("\nSensor de presenca ativado - \n\n")
		var_entrada_presenca = 1
		if saida_estados[4] == 1:	
			sistemaAlarme()
		else:
			if cont_pessoas == 0:
				GPIO.output(saidas[0], GPIO.HIGH)
				GPIO.output(saidas[1], GPIO.HIGH)
				print("Aguarde 15 segundos.\n")
	else:
		var_entrada_presenca = 0

def sensorJanela(channel):
	global var_entrada_janela
	if var_entrada_janela == 0:
		print("Sensor de janela ativado - \n\n")
		var_entrada_janela = 1
		if saida_estados[4] == 1 and cont_pessoas == 0:
			sistemaAlarme()
	else:
		var_entrada_janela = 0

def sensorPorta(channel):
	global var_entrada_porta
	if var_entrada_porta == 0:
		print("Sensor de porta ativado - \n\n")
		var_entrada_porta = 1
		if saida_estados[4] == 1 and cont_pessoas == 0:
			sistemaAlarme()
	else:
		var_entrada_porta = 1

def sensorFumaca(channel):
	global var_entrada_fumaca
	if var_entrada_fumaca == 0:
		var_entrada_fumaca = 1
		print("Sensor de fumaca ativado - \n\n")
		sistemaAlarme()
	else:
		var_entrada_fumaca = 0
		
GPIO.setup(saidas, GPIO.OUT)

GPIO.setup(entrada_janela, GPIO.IN)
GPIO.setup(entrada_contagem_entrada, GPIO.IN)
GPIO.setup(entrada_contagem_saida, GPIO.IN)
GPIO.setup(entrada_porta, GPIO.IN)
GPIO.setup(entrada_fumaca, GPIO.IN)
GPIO.setup(entrada_presenca, GPIO.IN)

GPIO.add_event_detect(entrada_porta, GPIO.BOTH, callback=sensorPorta)
GPIO.add_event_detect(entrada_janela, GPIO.BOTH, callback=sensorJanela)
GPIO.add_event_detect(entrada_contagem_entrada, GPIO.RISING, callback=sensorEntradaPessoa)
GPIO.add_event_detect(entrada_contagem_saida, GPIO.RISING, callback=sensorSaidaPessoa)
GPIO.add_event_detect(entrada_fumaca, GPIO.BOTH, callback=sensorFumaca)
GPIO.add_event_detect(entrada_presenca, GPIO.BOTH, callback=sensorPresenca)

def ligaDesligaLPA(msg2):
	print(type(msg2))
	if msg2 == 1:
		print('entro no 1')
		GPIO.output(saidas[0], GPIO.HIGH)
		saida_estados[0] = 1

	elif msg2 == 2:
		print('entro no 2')
		GPIO.output(saidas[0], GPIO.LOW)
		saida_estados[0] = 0
	
	elif msg2 == 3:
		print('entro no 3')
		GPIO.output(saidas[1], GPIO.HIGH)
		saida_estados[1] = 1

	elif msg2 == 4:
		print('entro no 4')
		GPIO.output(saidas[1], GPIO.LOW)
		saida_estados[1] = 0
	
	elif msg2 == 5:
		GPIO.output(saidas[2], GPIO.HIGH)
		saida_estados[2] = 1

	elif msg2 == 6:
		GPIO.output(saidas[2], GPIO.LOW)
		saida_estados[2] = 0

	elif msg2 == 7:
		GPIO.output(saidas[3], GPIO.HIGH)
		saida_estados[3] = 1

	elif msg2 == 8:
		GPIO.output(saidas[3], GPIO.LOW)
		saida_estados[3] = 0

	elif msg2 == 9:
		saida_estados[4] = 1

	elif msg2 == 10:
		saida_estados[4] = 0

	elif msg2 == 11:
		GPIO.output(saidas[0], GPIO.HIGH)
		GPIO.output(saidas[1], GPIO.HIGH)
		GPIO.output(saidas[2], GPIO.HIGH)
		GPIO.output(saidas[3], GPIO.HIGH)
		GPIO.output(saidas[4], GPIO.HIGH)
		saida_estados[0] = 1
		saida_estados[1] = 1
		saida_estados[2] = 1
		saida_estados[3] = 1
		saida_estados[4] = 1

	elif msg2 == 12:
		GPIO.output(saidas[0], GPIO.LOW)
		GPIO.output(saidas[1], GPIO.LOW)
		GPIO.output(saidas[2], GPIO.LOW)
		GPIO.output(saidas[3], GPIO.LOW)
		GPIO.output(saidas[4], GPIO.LOW)
		saida_estados[0] = 0
		saida_estados[1] = 0
		saida_estados[2] = 0
		saida_estados[3] = 0
		saida_estados[4] = 0

def estadoSaidas():
	if saida_estados[0] == 0:
		print("\n-> lampada 01 esta inativa.")

	else: 
		print("\n-> lampada 01 esta ligada.")

	if saida_estados[1] == 0:
		print("\n-> lampada 02 esta inativa.")

	else: 
		print("\n-> lampada 02 esta ligada.")

	if saida_estados[2] == 0:
		print("\n-> ar condicionado esta inativo.")

	else: 
		print("\n-> ar condicionado esta ligado.")

	if saida_estados[3] == 0:
		print("\n-> projetor esta inativo.")

	else: 
		print("\n-> projetor esta ligado.")
	
	if saida_estados[4] == 0:
		print("\n-> sistema de alarme esta inativo.")

	else: 
		print("\n-> sistema de alarme esta ligado.\n")

def estadosEntradas():		
	if var_entrada_fumaca == 0:
		print("\n-> Sensor de fumaca esta inativo.")

	else: 
		print("\n-> Sensor de fumaca esta ligado.")
	
	if var_entrada_janela == 0:
		print("\n-> Sensor da janela esta inativo.")

	else: 
		print("\n-> Sensor da janela esta ligado.")

	if var_entrada_porta == 0:
		print("\n-> Sensor da porta esta inativo.")

	else: 
		print("\n-> Sensor da porta esta ligado.")

	if var_entrada_presenca == 0:
		print("\n-> Sensor de presenca esta inativo.")

	else: 
		print("\n-> Sensor de presenca esta ligado.")