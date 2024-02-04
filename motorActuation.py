import RPi.GPIO as GPIO  #Import library
import time

GPIO.setmode(GPIO.BCM)  #Set pin
AIN1 = 17
AIN2 = 18
backLeftF = AIN1
backLeftB = AIN2


BIN1 = 22 
BIN2 = 23
backRightB = BIN1
backRightF = BIN2
#Modification adding the two other motors
CIN1 = 9 #pin number where motors are connected
CIN2 = 25
frontRightB = CIN1
frontRightF = CIN2

DIN1 = 11
DIN2 = 8
frontLeftF = DIN1
frontLeftB = DIN2

#need to specify which letter (a,b,c or d) belong to each motor number (1...4)



GPIO.setwarnings(False)   #Remove warning
GPIO.setup(backLeftF, GPIO.OUT)  #Set pin to output mode
GPIO.output(backLeftF, 0)
GPIO.setup(backLeftB, GPIO.OUT)
GPIO.output(backLeftB, 0)
GPIO.setup(backRightB, GPIO.OUT)
GPIO.output(backRightB, 0)
GPIO.setup(backRightF, GPIO.OUT)
GPIO.output(backRightF, 0)

GPIO.setup(frontRightB, GPIO.OUT)  #Second set of motors
GPIO.output(frontRightB, 0)
GPIO.setup(frontRightF, GPIO.OUT)
GPIO.output(frontRightF, 0)
GPIO.setup(frontLeftF, GPIO.OUT)
GPIO.output(frontLeftF, 0)
GPIO.setup(frontLeftB, GPIO.OUT)
GPIO.output(frontLeftB, 0)


def forward():  #Motor rotation
    #A and B are the different motors, ___1 refers for forward, ___2 refers for backware
    GPIO.output(backLeftF,0)
    GPIO.output(backLeftB,0)
    GPIO.output(backRightB,0)
    GPIO.output(backRightF,0)
    #Second set of motors
    GPIO.output(frontRightB,0)
    GPIO.output(frontRightF,0)
    GPIO.output(frontLeftF,1)
    GPIO.output(frontLeftB,0)

def backward():  #Motor rotation
    #A and B are the different motors, 1 and 2 are different directions
    GPIO.output(backLeftF,0)
    GPIO.output(backLeftB,1)
    GPIO.output(backRightB,0)
    GPIO.output(backRightF,1)
    #Second set of motors
    GPIO.output(frontRightB,0)
    GPIO.output(frontRightF,1)
    GPIO.output(frontLeftF,0)
    GPIO.output(frontLeftB,1)

def left():  #Motor rotation
    #Still needs to be modified
    GPIO.output(backLeftF,1)
    GPIO.output(backLeftB,0)
    GPIO.output(backRightB,1)
    GPIO.output(backRightF,0)
    GPIO.output(frontRightB,1)
    GPIO.output(frontRightF,0)
    GPIO.output(frontLeftF,1)
    GPIO.output(frontLeftB,0)

def right():  #still needs to be modified
    GPIO.output(backLeftF,1)
    GPIO.output(backLeftB,0)
    GPIO.output(backRightB,1)
    GPIO.output(backRightF,0)
    GPIO.output(frontRightB,1)
    GPIO.output(frontRightF,0)
    GPIO.output(frontLeftF,1)
    GPIO.output(frontLeftB,0)
    
def stop():   #Motor stop
    GPIO.output(backLeftF,0)
    GPIO.output(backLeftB,0)
    GPIO.output(backRightB,0)
    GPIO.output(backRightF,0)
    #Second set of motors
    GPIO.output(frontRightB,0)
    GPIO.output(frontRightF,0)
    GPIO.output(frontLeftF,0)
    GPIO.output(frontLeftB,0)


forward()   #Motor rotation
# time.sleep(5)   #Delay 5 seconds
# right()   #Motor rotation
# time.sleep(5)   #Delay 5 seconds
# backward()   #Motor rotation
# time.sleep(5)   #Delay 5 seconds
# left()   #Motor rotation
time.sleep(5)   #Delay 5 seconds
stop()   #stop
GPIO.cleanup()  #clean up