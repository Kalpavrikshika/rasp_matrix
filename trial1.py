import time
import RPi.GPIO as GPIO

def __init__():

               
		COL1=17
		COL2=4
		COL3=22
		COL4=5
		ROWA=21
		ROWB=20
		ROWC=16
		ROWD=12
		sleeptime=1		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(COL1,GPIO.OUT)
		GPIO.setup(COL2,GPIO.OUT)
		GPIO.setup(COL3,GPIO.OUT)
		GPIO.setup(COL4,GPIO.OUT)
		GPIO.setup(ROWA,GPIO.OUT)
		GPIO.setup(ROWB,GPIO.OUT)
		GPIO.setup(ROWC,GPIO.OUT)
		GPIO.setup(ROWD,GPIO.OUT)


def clear():
	GPIO.setup(COL1,GPIO.LOW)
	GPIO.setup(COL2,GPIO.LOW)
	GPIO.setup(COL3,GPIO.LOW)
	GPIO.setup(COL4,GPIO.LOW)
	GPIO.setup(ROWA,GPIO.LOW)
	GPIO.setup(ROWB,GPIO.LOW)
	GPIO.setup(ROWC,GPIO.LOW)
	GPIO.setup(ROWD,GPIO.LOW)

def bluepill():

	while 1:
		clear()		
		GPIO.output(COL1,GPIO.HIGH)
		GPIO.output(ROWA,GPIO.LOW)
		GPIO.output(ROWB,GPIO.LOW)
		GPIO.output(ROWC,GPIO.LOW)
		GPIO.output(ROWD,GPIO.LOW)
		time.sleep(sleeptime)

		clear()
		GPIO.output(COL2,GPIO.HIGH)
		GPIO.output(ROWA,GPIO.HIGH)
		GPIO.output(ROWB,GPIO.HIGH)
		GPIO.output(ROWC,GPIO.HIGH)
		GPIO.output(ROWD,GPIO.LOW)
		time.sleep(sleeptime)

		clear()
		GPIO.output(COL3,GPIO.HIGH)
		GPIO.output(ROWA,GPIO.LOW)
		GPIO.output(ROWB,GPIO.HIGH)
		GPIO.output(ROWC,GPIO.HIGH)
		GPIO.output(ROWD,GPIO.HIGH)
		time.sleep(sleeptime)

		clear()
		#GPIO.output(COL4,GPIO.HIGH)
		#GPIO.output(ROWA,GPIO.LOW)
		#GPIO.output(ROWB,GPIO.LOW)
		#GPIO.output(ROWC,GPIO.LOW)
		#GPIO.output(ROWD,GPIO.LOW)
		#time.sleep(sleeptime)

def main():
	
	bluepill()

if __name__=="__main__":
        main()
	 
