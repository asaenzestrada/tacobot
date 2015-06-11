import threading
import time
from BrickPi import *

BrickPiSetup()

motor1 = PORT_A #girar
motor2 = PORT_B #agacharse
motor3 = PORT_C #garra
sensor1 = PORT_1 #touch
BrickPi.SensorType[sensor1] = TYPE_SENSOR_TOUCH
BrickPi.MotorEnable[motor1] = 1
BrickPi.MotorEnable[motor2] = 1
BrickPi.MotorEnable[motor3] = 1


BrickPiSetupSensors()
#que el ciclo comience con el cambio del sensor.
#cambiar el estado total por el estado del sensor.
while True:
    result = BrickPiUpdateValues()
    if not result:
        if BrickPi.Sensor[sensor1]:
            hazTaco()
            
        #else:
            #closeClawDegree()

        
    time.sleep(0.01)

    
    
class ServoMotors():
    def motorDown(self):
    BrickPi.MotorSpeed[motor2] = 100
    return

    def motorUp(self):
        BrickPi.MotorSpeed[motor2] = -100
        return
    
    def motorDownDegree(self):
        motorRotateDegree([5000],[40], [motor2],0)
        return
    
    def motorUpDegree(self):
        motorRotateDegree([500],[-20], [motor2],0)
        return
    
    def openClaw(self):
        motorRotateDegree([400],[100], [motor3],0)
        return
    
    def closeClaw(self):
        motorRotateDegree([-600],[-100], [motor3],0)
        return
    
    def rotateLeft(self):
        motorRotateDegree([1000],[5000],[motor1],0)
        return
    
    def rotateRight(self):
        motorRotateDegree([-1000],[-5000],[motor1],0)
        return
    
    def hazTaco(self):
        
        
        
        
        print("Intentando girar a la derecha") 
        rotateRight(self)
        print("Ya gire")
        time.sleep(0.01)
    
        print("Intentando moverme para abajo")
        motorDownDegree(self)
        print("Ya baje")
        time.sleep(0.01)
    
        print("Tratando de abrir mi garra")
        openClaw(self)
        print("Ya se abrio")
        time.sleep(0.01)
    
        print("Cerrando mi garra")
        closeClaw(self)
        print("Ya se cerro")
        time.sleep(0.01)
    
        print("Moviendome para arriba")
        motorUpDegree(self)
        print("Ya subi")
        time.sleep(0.01)
    
        print("Intentando girar a la izquierda")
        rotateLeft(self)
        print("Ya gire")
        time.sleep(0.01)
    
        print("Abriendo mi garra")
        openClaw(self)
        print("Ya se abrio")
        time.sleep(5)
    
        print("Cerrando mi garra")
        closeClaw(self)
        print("Ya se cerro")
        time.sleep(0.01)
        print("Ya esta su taco")
        return
    
    
