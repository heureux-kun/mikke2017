import wiringpi as pi
import time

pin_num =  5

pi.wiringPiSetupGpio()
pi.pinMode(pin_num, pi.OUTPUT)

try:
    pi.digitalWrite(pin_num,pi.HIGH)
    time.sleep(1)
    pi.digitalWrite(pin_num,pi.LOW)
    time.sleep(3)
except KeyboardInterrupt:
    pass
