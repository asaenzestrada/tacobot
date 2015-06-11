import string

class ServoMotors():
    
    
	def servo311(ang):
		import wiringpi2 as lib
		lib.wiringPiSetup()
		lib.pinMode(1,2)
		lib.pwmSetMode(0)
		lib.pwmSetClock(192)
		print("Angulo = " + str(ang))
		ent = int(ang)
		y = ent+60
		lib.pwmWrite(1,y)


ServoMotors.servo311(180)
