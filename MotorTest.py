import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
Motor1A = 23
Motor1B = 24
Motor1E = 25
 
Motor2A = 11
Motor2B = 9
Motor2E = 10
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
pwm1=GPIO.PWM(Motor1E,100)
pwm1.start(40)
pwm2=GPIO.PWM(Motor2E,100)
pwm2.start(0)
print ("Going forwards")
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
 
GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)
 
sleep(0.5)
 
print("Going backwards")
#GPIO.output(Motor1A,GPIO.LOW)
#GPIO.output(Motor1B,GPIO.HIGH)
#GPIO.output(Motor1E,GPIO.HIGH)
 
#GPIO.output(Motor2A,GPIO.LOW)
#GPIO.output(Motor2B,GPIO.HIGH)
#GPIO.output(Motor2E,GPIO.HIGH)
 
#sleep(2)
 
print("Now stop")
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
 

