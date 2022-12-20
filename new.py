import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarning(False)

leds = [18,23,24,25,8]

GPIO.setup(leds, GPIO.OUT)

def menu(msg):
	print("Seja bem-vindo ao menu da sala mais\n")
	
	print("1 - Ligar lampada")
	print("2 - Ligar ar condicionado")
	print("3 - EStados em tempo real")

	if msg == 1:
		print("hora de ligar a lampada")
# mim no like it. quero que printe sempre os estados
# no inicio do while true do distribuido.py
#def estadoInicialLeds():
	global counter
#	GPIO.output(leds, GPIO.LOW)

#	print("Conador?")


while True:
	counter = 0
	while counter < 8:
		GPIO.output(leds, (
			GPIO.HIGH if counter & 0b0100 else GPIO.LOW,
			GPIO.HIGH if counter & 0b0010 else GPIO.LOW,
			GPIO.HIGH if counter & 0b0001 else GPIO.LOW,
			)
		)
		counter += 1
		sleep(1)
