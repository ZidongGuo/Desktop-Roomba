import time
import board
import busio
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33

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

def Read_Angle():
    print("Turning Angle is")

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
    print("go forward")

def Backward():
    print("go backward")
