import wiringpi as pi
import time

pin_num =  26

pi.wiringPiSetupGpio()
pi.pinMode(pin_num, pi.OUTPUT)
pi.digitalWrite(pin_num, pi.LOW)

try:
    pi.digitalWrite(pin_num,pi.HIGH)
    time.sleep(0.1)
    pi.digitalWrite(pin_num,pi.LOW)
    time.sleep(0.1)
except KeyboardInterrupt:
    pass

