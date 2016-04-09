import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

COL1=4
COL2=17
COL3=22
COL4=5
COL5=6
COL6=26
ROWA=18
ROWB=23
ROWC=12
ROWD=16
ROWE=20
ROWF=21
sleeptime=1
GPIO.setmode(GPIO.BCM)
GPIO.setup(COL1,GPIO.OUT)
GPIO.setup(COL2,GPIO.OUT)
GPIO.setup(COL3,GPIO.OUT)
GPIO.setup(COL4,GPIO.OUT)
GPIO.setup(COL5,GPIO.OUT)
GPIO.setup(COL6,GPIO.OUT)
GPIO.setup(ROWA,GPIO.OUT)
GPIO.setup(ROWB,GPIO.OUT)
GPIO.setup(ROWC,GPIO.OUT)
GPIO.setup(ROWD,GPIO.OUT)
GPIO.setup(ROWE,GPIO.OUT)
GPIO.setup(ROWF,GPIO.OUT)

GPIO.setup(COL1,GPIO.LOW)
GPIO.setup(COL2,GPIO.LOW)
GPIO.setup(COL3,GPIO.LOW)
GPIO.setup(COL4,GPIO.LOW)
GPIO.setup(COL5,GPIO.LOW)
GPIO.setup(COL6,GPIO.LOW)
GPIO.setup(ROWA,GPIO.LOW)
GPIO.setup(ROWB,GPIO.LOW)
GPIO.setup(ROWC,GPIO.LOW)
GPIO.setup(ROWD,GPIO.LOW)
GPIO.setup(ROWE,GPIO.LOW)
GPIO.setup(ROWF,GPIO.LOW)


def A():
    A=1

    while A<500:
        
        GPIO.setup(COL1,GPIO.HIGH)
        GPIO.setup(COL2,GPIO.LOW)
        GPIO.setup(COL3,GPIO.LOW)
        GPIO.setup(COL4,GPIO.LOW)
        GPIO.setup(COL5,GPIO.LOW)
        GPIO.setup(COL6,GPIO.LOW)
        GPIO.setup(ROWA,GPIO.LOW)
        GPIO.setup(ROWB,GPIO.HIGH)
        GPIO.setup(ROWC,GPIO.HIGH)
        GPIO.setup(ROWD,GPIO.HIGH)
        GPIO.setup(ROWE,GPIO.HIGH)
        GPIO.setup(ROWF,GPIO.HIGH)
        print ('hellow')
        time.sleep(2)

        GPIO.setup(COL1,GPIO.LOW)
        GPIO.setup(COL2,GPIO.HIGH)
        GPIO.setup(COL3,GPIO.LOW)
        GPIO.setup(COL4,GPIO.LOW)
        GPIO.setup(COL5,GPIO.LOW)
        GPIO.setup(COL6,GPIO.LOW)
        GPIO.setup(ROWA,GPIO.HIGH)
        GPIO.setup(ROWB,GPIO.LOW)
        GPIO.setup(ROWC,GPIO.LOW)
        GPIO.setup(ROWD,GPIO.LOW)
        GPIO.setup(ROWE,GPIO.LOW)
        GPIO.setup(ROWF,GPIO.LOW)
        
        time.sleep(2)

        GPIO.setup(COL1,GPIO.LOW)
        GPIO.setup(COL2,GPIO.LOW)
        GPIO.setup(COL3,GPIO.HIGH)
        GPIO.setup(COL4,GPIO.LOW)
        GPIO.setup(COL5,GPIO.LOW)
        GPIO.setup(COL6,GPIO.LOW)
        GPIO.setup(ROWA,GPIO.LOW)
        GPIO.setup(ROWB,GPIO.HIGH)
        GPIO.setup(ROWC,GPIO.HIGH)
        GPIO.setup(ROWD,GPIO.LOW)
        GPIO.setup(ROWE,GPIO.HIGH)
        GPIO.setup(ROWF,GPIO.HIGH)
        
        time.sleep(2)

        GPIO.setup(COL1,GPIO.LOW)
        GPIO.setup(COL2,GPIO.LOW)
        GPIO.setup(COL3,GPIO.LOW)
        GPIO.setup(COL4,GPIO.HIGH)
        GPIO.setup(COL5,GPIO.LOW)
        GPIO.setup(COL6,GPIO.LOW)
        GPIO.setup(ROWA,GPIO.LOW)
        GPIO.setup(ROWB,GPIO.HIGH)
        GPIO.setup(ROWC,GPIO.HIGH)
        GPIO.setup(ROWD,GPIO.LOW)
        GPIO.setup(ROWE,GPIO.HIGH)
        GPIO.setup(ROWF,GPIO.HIGH)
        
        time.sleep(2)

        GPIO.setup(COL1,GPIO.LOW)
        GPIO.setup(COL2,GPIO.LOW)
        GPIO.setup(COL3,GPIO.LOW)
        GPIO.setup(COL4,GPIO.LOW)
        GPIO.setup(COL5,GPIO.HIGH)
        GPIO.setup(COL6,GPIO.LOW)
        GPIO.setup(ROWA,GPIO.HIGH)
        GPIO.setup(ROWB,GPIO.LOW)
        GPIO.setup(ROWC,GPIO.LOW)
        GPIO.setup(ROWD,GPIO.LOW)
        GPIO.setup(ROWE,GPIO.LOW)
        GPIO.setup(ROWF,GPIO.LOW)
        
        time.sleep(2)

        GPIO.setup(COL1,GPIO.LOW)
        GPIO.setup(COL2,GPIO.LOW)
        GPIO.setup(COL3,GPIO.LOW)
        GPIO.setup(COL4,GPIO.LOW)
        GPIO.setup(COL5,GPIO.LOW)
        GPIO.setup(COL6,GPIO.HIGH)
        GPIO.setup(ROWA,GPIO.HIGH)
        GPIO.setup(ROWB,GPIO.HIGH)
        GPIO.setup(ROWC,GPIO.HIGH)
        GPIO.setup(ROWD,GPIO.HIGH)
        GPIO.setup(ROWE,GPIO.HIGH)
        GPIO.setup(ROWF,GPIO.HIGH)
        
        time.sleep(2)

        A+=1

#END OF 'A'
while 1:
    
    A()
