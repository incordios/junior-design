from time import sleep
import RPi.GPIO as GPIO
from gpiozero import LED
from gpiozero.pins.rpigpio import RPiGPIOFactory

GPIO.setwarnings(False)

# PWM Frequency
pwmFreq = 100

# Setup pins
LEDPIN = 24
TESTMODE = 25
STBY = 23
BIN1 = 18
BIN2 = 15
PWMB = 14

# Board Mode
GPIO.setmode(GPIO.BCM)
factory = RPiGPIOFactory()
led = LED(LEDPIN, pin_factory=factory)
GPIO.setup(TESTMODE, GPIO.IN)   #TESTMODE
GPIO.setup(STBY, GPIO.OUT)  #STBY
GPIO.setup(BIN1, GPIO.OUT)  #BIN1
GPIO.setup(BIN2, GPIO.OUT)  #BIN2

GPIO.setup(PWMB, GPIO.OUT)  #PWMB
pwmb = GPIO.PWM(PWMB, pwmFreq) 
pwmb.start(100)

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(22, GPIO.IN)   #TESTMODE
# led = LED(24)
# # GPIO.setup(18, GPIO.OUT)  #LED
# GPIO.setup(16, GPIO.OUT)  #STBY
# GPIO.setup(12, GPIO.OUT)  #BIN1
# GPIO.setup(10, GPIO.OUT)  #BIN2
# 
# GPIO.setup(8, GPIO.OUT)  #PWMB
# pwmb = GPIO.PWM(8, pwmFreq) 
# pwmb.start(100)

# Functions
def forward(spd):
    runMotor(spd, 0)

def backward(spd):
    runMotor(spd, 1)

def runMotor(spd, direction):
    GPIO.output(STBY, GPIO.HIGH);
    in1 = GPIO.HIGH
    in2 = GPIO.LOW

    if(direction == 1):
        in1 = GPIO.LOW
        in2 = GPIO.HIGH

    GPIO.output(BIN1, in1)
    GPIO.output(BIN2, in2)
    pwmb.ChangeDutyCycle(spd)

def motorStop():
    pwmb.ChangeDutyCycle(0)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)

def oscillate(time):
    for _ in range(time):
        forward(13)
        sleep(0.040)
        motorStop()
        sleep(3)
        backward(15)
        sleep(0.05)
        motorStop()
        sleep(3)

def testMode():
    return (GPIO.input(TESTMODE) == 1)

def ledOn():
    led.on()

def ledOff():
    led.off()