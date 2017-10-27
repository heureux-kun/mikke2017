import wiringpi as pi
import time

SOLENOID_PIN =  16

pi.wiringPiSetupGpio()
pi.pinMode(SOLENOID_PIN, pi.OUTPUT)
pi.digitalWrite(SOLENOID_PIN, pi.LOW)

try:
    pi.digitalWrite(SOLENOID_PIN,pi.HIGH)
    time.sleep(0.1)
    pi.digitalWrite(SOLENOID_PIN,pi.LOW)
    time.sleep(0.1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
