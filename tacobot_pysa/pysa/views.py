from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
import time
from BrickPi import *


BrickPiSetup()

# Create your views here.
@csrf_protect
def system(request):
	if request.method == 'POST':
		for n in range(int(request.POST.get('q', '0'))):
			a = n
			hazTaco()
		return render_to_response('index.html', dict(), context_instance=RequestContext(request))
	return render_to_response('index.html', dict(), context_instance=RequestContext(request))

motor1 = PORT_A #girar
motor2 = PORT_B #agacharse	
motor3 = PORT_C #garra
sensor1 = PORT_1 #touch
BrickPi.SensorType[sensor1] = TYPE_SENSOR_TOUCH
BrickPi.MotorEnable[motor1] = 1
BrickPi.MotorEnable[motor2] = 1
BrickPi.MotorEnable[motor3] = 1
BrickPiSetupSensors()
	
	
def motorDown():
	BrickPi.MotorSpeed[motor2] = 100
	return

def motorUp():
	BrickPi.MotorSpeed[motor2] = -100
	return

def motorDownDegree():
	motorRotateDegree([5000],[40], [motor2],0)
	return

def motorUpDegree():
	motorRotateDegree([500],[-20], [motor2],0)
	return

def openClaw():
	motorRotateDegree([400],[100], [motor3],0)
	return

def closeClaw():
	motorRotateDegree([-600],[-100], [motor3],0)
	return

def rotateLeft():
	motorRotateDegree([1000],[5000],[motor1],0)
	return

def rotateRight():
	motorRotateDegree([-1000],[-5000],[motor1],0)
	return

def hazTaco():
	
	print("Intentando girar a la derecha") 
	rotateRight()
	print("Ya gire")
	time.sleep(0.01)

	print("Intentando moverme para abajo")
	motorDownDegree()
	print("Ya baje")
	time.sleep(0.01)

	print("Tratando de abrir mi garra")
	openClaw()
	print("Ya se abrio")
	time.sleep(2)

	print("Cerrando mi garra")
	closeClaw()
	print("Ya se cerro")
	time.sleep(0.01)

	print("Moviendome para arriba")
	motorUpDegree()
	print("Ya subi")
	time.sleep(0.01)

	print("Intentando girar a la izquierda")
	rotateLeft()
	print("Ya gire")
	time.sleep(0.01)

	print("Abriendo mi garra")
	openClaw()
	print("Ya se abrio")
	time.sleep(5)

	print("Cerrando mi garra")
	closeClaw()
	print("Ya se cerro")
	time.sleep(0.01)
	print("Ya esta su taco")
	return
	time.sleep(0.01)