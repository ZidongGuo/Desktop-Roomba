import DesktopRoomba
import sys
import time
from time import sleep
import RPi.GPIO as GPIO
DesktopRoomba.setup()
print("Power of the robot is ", DesktopRoomba.Power)
DesktopRoomba.Read_DistanceL()
DesktopRoomba.Read_DistanceR()
DesktopRoomba.Read_DistanceF()
#a=DesktopRoomba.Read_IR_Reflectance()
#print (a)
IMU=DesktopRoomba.Setup_IMU()
#while True:
#    a=DesktopRoomba.Read_Angle(IMU)

#    print(a)
#    print(DesktopRoomba.Read_Acceleration(IMU))

a=DesktopRoomba.Read_Angle(IMU)
b=abs(a[0])+abs(a[1])+abs(a[2])
print(b)
#DesktopRoomba.Set_DutyCycle()
#DesktopRoomba.Set_PWM_Frequency()
#DesktopRoomba.Away_from_edges()
#DesktopRoomba.Turn_Left(0.5)
#DesktopRoomba.Turn_Right(0.8)
#DesktopRoomba.Forward(50)
#sleep(1.5)
#DesktopRoomba.Stop()
#sleep(2)
#DesktopRoomba.Backward(50)
#sleep(1.5)
#DesktopRoomba.Stop()
#sleep(2)
#print("Power of the robot is ", DesktopRoomba.Power)
#DesktopRoomba.power()
GPIO.cleanup()
