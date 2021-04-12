import time
import board
import busio
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33
import RPi.GPIO as GPIO
from time import sleep

def setup():
    print("All programs have been set up successfully!")
    return True

def Read_Ultrasonic_Distance():
    print("Distance from the ultrasonic sensors is ")

def Read_IR_Reflectance():
    print("The reflectance is ")

def Setup_IMU():
    i2c = busio.I2C(board.SCL, board.SDA)
    s33 = LSM6DS33(i2c)
    print("IMU is set up")
    return s33

def Read_Angle(IMU):
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (IMU.gyro))
    return IMU.gyro

def Read_Acceleration(IMU):
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(IMU.acceleration))
    return IMU.acceleration

def Set_DutyCycle():
    print("Duty Cycle is set to be")

def Set_PWM_Frequency():
    print("PWM is set to be")

def Away_from_edges():
    print("Move away from edges")

def Turn_Left():
    print("Turn Left")
def Turn_Right():
    print("Turn Right")

def Forward():
    GPIO.setmode(GPIO.BOARD)
    Motor1A = 16
    Motor1B = 18
    Motor1E = 22
    Motor2A = 23
    Motor2B = 21
    Motor2E = 19
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)
    print("go forward")
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
def Backward():
    print("go backward")
