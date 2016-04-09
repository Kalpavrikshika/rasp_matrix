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

def L():
    L=0
    while L<500:
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.HIGH)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.LOW)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.HIGH)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.HIGH)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.HIGH)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.HIGH)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            L+=1
#END OF L

def M():
    M=0
    while M<500:
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.HIGH)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.LOW)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.HIGH)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.LOW)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.HIGH)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.LOW)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.HIGH)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.HIGH)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.HIGH)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.LOW)
            
            time.sleep(0.001)
            
            M+=1
#END OF M

def T():
    T=0
    while T<500:
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.HIGH)
            GPIO.setup(ROWA,GPIO.HIGH)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.HIGH)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.HIGH)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.HIGH)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.HIGH)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.HIGH)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.HIGH)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.HIGH)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.HIGH)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            T+=1
#END OF T

def R():
    R=0
    while R<500:
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.HIGH)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.LOW)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.HIGH)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.LOW)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.HIGH)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.HIGH)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.LOW)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.HIGH)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            R+=1
#END OF R

def I():
    I=0
    while I<500:
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.HIGH)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.LOW)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.HIGH)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.HIGH)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.HIGH)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.HIGH)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.HIGH)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.HIGH)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.HIGH)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.LOW)
            
            time.sleep(0.001)
            
            I+=1
#END OF I

def X():
    X=0
    while X<500:
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.HIGH)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.LOW)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.HIGH)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.HIGH)
            GPIO.setup(ROWB,GPIO.LOW)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.HIGH)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.HIGH)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.LOW)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.LOW)
            GPIO.setup(COL2,GPIO.HIGH)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.LOW)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.LOW)
            
            time.sleep(0.001)
            
            GPIO.setup(COL1,GPIO.HIGH)
            GPIO.setup(COL2,GPIO.LOW)
            GPIO.setup(COL3,GPIO.LOW)
            GPIO.setup(COL4,GPIO.LOW)
            GPIO.setup(COL5,GPIO.LOW)
            GPIO.setup(ROWA,GPIO.HIGH)
            GPIO.setup(ROWB,GPIO.HIGH)
            GPIO.setup(ROWC,GPIO.HIGH)
            GPIO.setup(ROWD,GPIO.HIGH)
            
            time.sleep(0.001)
            
            X+=1
#END OF X
      
        
while 1:       
    #L()
    #E()
    #D()
    #M()
    A()
    B()
    C()
    D()
    E()
    #T()
    #R()
    #I()
    #X()

















