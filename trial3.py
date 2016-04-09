import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

               
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

GPIO.setup(COL1,GPIO.LOW)
GPIO.setup(COL2,GPIO.LOW)
GPIO.setup(COL3,GPIO.LOW)
GPIO.setup(COL4,GPIO.LOW)
GPIO.setup(ROWA,GPIO.LOW)
GPIO.setup(ROWB,GPIO.LOW)
GPIO.setup(ROWC,GPIO.LOW)
GPIO.setup(ROWD,GPIO.LOW)

def K():
    K=1
    
    while K<500:
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)
        K+=1

#END OF K

def H():
    H=1
    while H<500:
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)
        H+=1

#END OF H
        


def A():
    A=1
    while A<500:
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)
        A+=1


#END OF A



def C():
    C=1
    
    while C<500:
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)
        C+=1

#END OF C



def T():
    T=1
    while T<500:
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)
        T+=1

#END OF T




def O():
    O=1
    while O<500:
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)  
        O+=1
        
  #END OF O      




def B():
    B=1
    while B<500:
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)  
        B+=1


#END OF B

def H():
    H=1
    while H<500:
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)
        H+=1

#END OF H

def D():
    D=1
    while D<500:
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
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
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)
        E+=1
#END OF E

def N():
    N=1
    
    while N<500:
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.HIGH)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)
    
        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.HIGH)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.HIGH)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.LOW)
        GPIO.output(COL2,GPIO.HIGH)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.HIGH)
        GPIO.output(ROWB,GPIO.HIGH)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.HIGH)
    
        time.sleep(0.001)

        GPIO.output(COL1,GPIO.HIGH)
        GPIO.output(COL2,GPIO.LOW)
        GPIO.output(COL3,GPIO.LOW)
        GPIO.output(COL4,GPIO.LOW)
        GPIO.output(ROWA,GPIO.LOW)
        GPIO.output(ROWB,GPIO.LOW)
        GPIO.output(ROWC,GPIO.LOW)
        GPIO.output(ROWD,GPIO.LOW)
    
        time.sleep(0.001)
        N+=1

#END OF C
        
while 1:       
    H()
    A()
    C()
    K()
    A()
    T()
    H()
    O()
    N()
    #D()
    #B()
    #E()
    #F()

















