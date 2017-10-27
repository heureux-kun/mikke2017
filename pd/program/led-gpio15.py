import RPi. GPIO as GPIO
from time import sleep

pin_num = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_num,GPIO.OUT)

try:
    c = 0
    t = 3
    n = 1
    while c < n:
        GPIO.output(pin_num,GPIO.HIGH)
        sleep(t)
        c += 1
                
except KeyboardInterrupt:
    pass

GPIO.cleanup()
