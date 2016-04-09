import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)


               

COL1=17
COL2=4
COL3=22
COL4=5
COL5=13
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
GPIO.setup(COL5,GPIO.OUT)
GPIO.setup(ROWA,GPIO.OUT)
GPIO.setup(ROWB,GPIO.OUT)
GPIO.setup(ROWC,GPIO.OUT)
GPIO.setup(ROWD,GPIO.OUT)



GPIO.setup(COL1,GPIO.LOW)
GPIO.setup(COL2,GPIO.LOW)
GPIO.setup(COL3,GPIO.LOW)
GPIO.setup(COL4,GPIO.LOW)
GPIO.setup(COL5,GPIO.LOW)
GPIO.setup(ROWA,GPIO.LOW)
GPIO.setup(ROWB,GPIO.LOW)
GPIO.setup(ROWC,GPIO.LOW)
GPIO.setup(ROWD,GPIO.LOW)



def A():
    A=1
    
    while A<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        
        
        A+=1

#END OF A

def B():
    B=1
    
    while B<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        
        
        B+=1

#END OF B

def C():
    C=1
    
    while C<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        
        
        C+=1

#END OF C
def D():
    D=1
    
    while D<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        
        
        D+=1

#END OF D        

def E():
    E=1
    
    while E<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        
        
        E+=1

#END OF E

def F():
    F=1
    
    while F<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        
        
        F+=1

#END OF F        

def G():
    G=1
    
    while G<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        
        
        G+=1

#END OF G

def H():
    H=1
    
    while H<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        
        
        H+=1

#END OF H

def I():
    I=1
    
    while I<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        
        
        I+=1

#END OF I

def J():
    J=1
    
    while J<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        
        
        J+=1

#END OF J
def K():
    K=1
    
    while K<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        
        
        K+=1

#END OF K

def L():
    L=1
    
    while L<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        
        
        L+=1

#END OF L

def M():
    M=1
    
    while M<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        
        
        M+=1

#END OF M

def N():
    N=1
    
    while N<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        
        
        N+=1

#END OF N

def O():
    O=1
    
    while O<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        
        
        O+=1

#END OF O

def P():
    P=1
    
    while P<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        
        
        P+=1

#END OF P

def Q():
    Q=1
    
    while Q<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        
        
        Q+=1

#END OF Q

def R():
    R=1
    
    while R<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        
        
        R+=1

#END OF R

def S():
    S=1
    
    while S<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        
        
        S+=1

#END OF S

def T():
    T=1
    
    while T<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        
        
        T+=1

#END OF T

def U():
    U=1
    
    while U<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        
        
        U+=1

#END OF U

def V():
    V=1
    
    while V<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        
        
        V+=1

#END OF V

def W():
    W=1
    
    while W<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        
        
        W+=1

#END OF W

def X():
    X=1
    
    while X<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        
        
        X+=1

#END OF X

def Y():
    Y=1
    
    while Y<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        
        
        Y+=1

#END OF Y

def Z():
    Z=1
    
    while Z<500:
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
        

        time.sleep(0.001)
        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(COL5,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
        

        time.sleep(0.001)
        
        
        Z+=1

#END OF Z
while 1:       
    A()
    B()
    C()
    D()
    E()
    F()
    G()
    H()
    I()
    J()
    K()
    L()
    M()
    N()
    O()
    P()
    Q()
    R()
    S()
    T()
    U()
    V()
    W()
    X()
    Y()
    Z()

















