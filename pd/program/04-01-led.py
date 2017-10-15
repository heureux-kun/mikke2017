import RPi. GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)

try:
    c = 0
    s = 1
    t = 3
    while c < t:
        GPIO.output(25,GPIO.HIGH)
        sleep(s)
        GPIO.output(25,GPIO.LOW)
        sleep(s)
        c += 1
                
except KeyboardInterrupt:
    pass

GPIO.cleanup()
