import time
#import board
#import busio
#from adafruit_lsm6ds.lsm6ds33 import LSM6DS33
import RPi.GPIO as GPIO
from time import sleep
import sys

def setup():
    GPIO.cleanup()
    global Motor1A
    global Motor1B
    global Motor1E
    global Motor2A
    global Motor2B
    global Motor2E
    global pwm1
    global pwm2
    global EchoF
    global TrigF
    global EchoL
    global TrigL
    global EchoR
    global TrigR
    global GPIO_ir
    global Button
    global Power
    GPIO.setmode(GPIO.BCM)
    Button=26
    Power=0
    GPIO.setup(Button, GPIO.IN)
    Motor1A = 23
    Motor1B = 24
    Motor1E = 25
    Motor2A = 11
    Motor2B = 9
    Motor2E = 10
    GPIO_ir = 1
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)
    pwm1=GPIO.PWM(Motor1E,100)
    pwm2=GPIO.PWM(Motor2E,100)
    
    EchoF=15
    TrigF=14
    EchoR=20
    TrigR=21
    EchoL=12
    TrigL=16
    GPIO.setup(TrigF,GPIO.OUT)
    GPIO.setup(EchoF,GPIO.IN)
    GPIO.setup(TrigL,GPIO.OUT)
    GPIO.setup(EchoL,GPIO.IN)
    GPIO.setup(TrigR,GPIO.OUT)
    GPIO.setup(EchoR,GPIO.IN)
    print("All programs have been set up successfully!")
    def power_callback(input_pin):
      global Power
      if (Power==1):
        Power=0
        print("Power Off")
      elif (Power==0):
        Power=1
        print("Power On")
    GPIO.add_event_detect(Button, GPIO.RISING, callback=power_callback)
    return True

def Read_DistanceF():
    GPIO.output(TrigF, True)
    time.sleep(0.0001)
    GPIO.output(TrigF, False)
    StartTime=time.time()
    StopTime=time.time()
    while GPIO.input(EchoF)==0:
        StartTime=time.time()
    while GPIO.input(EchoF)==1:
        StopTime=time.time()
    TimePassed=StopTime-StartTime
    distance= TimePassed *17150
    #print("Distance from the front ultrasonic sensors is ", distance)
    return distance


def Read_DistanceL():
    GPIO.output(TrigL, True)
    time.sleep(0.00001)
    GPIO.output(TrigL, False)
    StartTime=time.time()
    StopTime=time.time()
    while GPIO.input(EchoL)==0:
        StartTime=time.time()
    while GPIO.input(EchoL)==1:
        StopTime=time.time()
    TimePassed=StopTime-StartTime
    distance= TimePassed *17150
    #print("Distance from the left ultrasonic sensors is ", distance)
    return distance

def Read_DistanceR():
    GPIO.output(TrigR, True)
    time.sleep(0.00001)
    GPIO.output(TrigR, False)
    StartTime=time.time()
    StopTime=time.time()
    while GPIO.input(EchoR)==0:
        StartTime=time.time()
    while GPIO.input(EchoR)==1:
        StopTime=time.time()
    TimePassed=StopTime-StartTime
    distance= TimePassed *17150
    #print("Distance from the right ultrasonic sensors is ", distance)
    return distance



# High value means low reflectance Low value means high reflectance
def Read_IR_Reflectance():
    GPIO.setup(GPIO_ir,GPIO.OUT)
    GPIO.output(GPIO_ir, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.setup(GPIO_ir,GPIO.IN)
    start=time.time()
    GPIO.wait_for_edge(GPIO_ir, GPIO.FALLING,timeout=200)
    end=time.time()
    print("%f seconds, %f us" %(end-start,1000000*(end-start) ) )
    return 1000000*(end-start)

def Setup_IMU():
    i2c = busio.I2C(board.SCL, board.SDA)
    s33 = LSM6DS33(i2c)
    print("IMU is set up")
    return s33

#def Read_Angle(IMU):
#    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (IMU.gyro))
#    return IMU.gyro

#def Read_Acceleration(IMU):
#    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(IMU.acceleration))
#    return IMU.acceleration

def Set_DutyCycle():
    print("Duty Cycle is set to be")

def Set_PWM_Frequency():
    print("PWM is set to be")

def Away_from_edges():
    print("Move away from edges")

def Turn_Left(Time):
    print("Turn Left")
    pwm1.start(40)
    pwm2.start(0)

    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)

    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)

    sleep(Time)
def Turn_Right(Time):
    print("Turn Right")
    pwm1.start(0)
    pwm2.start(40)

    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)

    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)

    sleep(Time)


def Forward(DC):
    print("go forward")
    #pwm1=GPIO.PWM(Motor1E,100)
    pwm1.start(DC)
    #pwm2=GPIO.PWM(Motor2E,100)
    pwm2.start(DC)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
def Backward(DC):
    pwm1.start(DC)
    pwm2.start(DC)
    print("go backward")
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)

    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)

def Stop():
    pwm1.stop()
    pwm2.stop()
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)
    print("Robot is stopped")
