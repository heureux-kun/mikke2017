import wiringpi as pi
import time

SOLENOID_PIN =  23

pi.wiringPiSetupGpio()
pi.pinMode(SOLENOID_PIN, pi.OUTPUT)
pi.digitalWrite(SOLENOID_PIN, pi.LOW)

while(True):
    pi.digitalWrite(SOLENOID_PIN,pi.HIGH)
    time.sleep(1)
    pi.digitalWrite(SOLENOID_PIN,pi.LOW)
    time.sleep(5)
