import RPi. GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)

try:
    c = 0
    t = 3
    n = 1
    while c < n:
        GPIO.output(25,GPIO.HIGH)
        sleep(t)
        c += 1
                
except KeyboardInterrupt:
    pass

GPIO.cleanup()
