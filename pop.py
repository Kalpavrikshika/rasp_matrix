import time
import RPi.GPIO as GPIO


GPIO.setwarnings(False)
COL1=17
ROWA=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(COL1,GPIO.OUT)
GPIO.setup(ROWA,GPIO.OUT)
time.sleep(0.9) 

GPIO.output(COL1,GPIO.HIGH)
GPIO.output(ROWA,GPIO.LOW)
print("hello")
    

