#For help with the motor driver, refer to: http://www.yahboom.net/study/Dual-MD-ModuleTT

import RPi.GPIO as GPIO  #Import library
import time

GPIO.setmode(GPIO.BCM)  #Set pin
AIN1 = 17
AIN2 = 18
BIN1 = 22 
BIN2 = 23
GPIO.setwarnings(False)   #Remove warning
GPIO.setup(AIN1, GPIO.OUT)  #Set pin to output mode
GPIO.output(AIN1, 0)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.output(AIN2, 0)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.output(BIN1, 0)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.output(BIN2, 0)

def forward():  #Motor rotation
    #The motors have different orientations, so while one spins one way, the other must spin in the 
    #opposite direction for them to move in the same direction together
    #AIN refers to one motor, while BIN refers to another motor
    GPIO.output(AIN1,1) #This turns on the motor in one direction
    GPIO.output(AIN2,0) #This turns on the motor in the opposite direction
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)
    
def stop():   #Motor stop
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,0)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,0)

forward()   #Motor rotation
time.sleep(5)   #Delay 5 seconds
stop()   #stop
GPIO.cleanup()  #clean up