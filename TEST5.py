import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(12,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

GPIO.setup(12,GPIO.HIGH)
GPIO.setup(27,GPIO.LOW)


