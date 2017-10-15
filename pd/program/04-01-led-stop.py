import RPi. GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)

try:
    GPIO.output(25,GPIO.LOW)
                
except KeyboardInterrupt:
    pass

GPIO.cleanup()
