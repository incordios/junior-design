from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# PWM Frequency
pwmFreq = 100

# Setup pins
GPIO.setup(22, GPIO.OUT)  #LED
GPIO.setup(18, GPIO.OUT)  #SPEAKER
GPIO.setup(16, GPIO.OUT)  #STBY
GPIO.setup(12, GPIO.OUT)  #BIN1
GPIO.setup(10, GPIO.OUT)  #BIN2
GPIO.setup(8, GPIO.OUT)  #PWMB
pwmb = GPIO.PWM(8, pwmFreq) # pin 13 to PWMB
pwmb.start(100)

# Functions
def forward(spd):
    runMotor(spd, 0)

def backward(spd):
    runMotor(spd, 1)

def runMotor(spd, direction):
    GPIO.output(16, GPIO.HIGH);
    in1 = GPIO.HIGH
    in2 = GPIO.LOW

    if(direction == 1):
        in1 = GPIO.LOW
        in2 = GPIO.HIGH

    GPIO.output(10, in1)
    GPIO.output(12, in2)
    pwmb.ChangeDutyCycle(spd)

def motorStop():
    pwmb.ChangeDutyCycle(0)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)

def oscillate(time):
    for i in range(time):
        forward(1)
        sleep(0.0038)
        motorStop()
        sleep(1)
        backward(20)
        sleep(0.02)
