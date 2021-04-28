import DesktopRoomba
import sys
import time
from time import sleep
DesktopRoomba.setup()
print("Power of the robot is ", DesktopRoomba.Power)
DesktopRoomba.Read_DistanceL()
DesktopRoomba.Read_DistanceR()

a=DesktopRoomba.Read_IR_Reflectance()
print (a)
IMU=DesktopRoomba.Setup_IMU()
DesktopRoomba.Read_Angle(IMU)
DesktopRoomba.Read_Acceleration(IMU)

DesktopRoomba.Set_DutyCycle()
DesktopRoomba.Set_PWM_Frequency()
DesktopRoomba.Away_from_edges()
DesktopRoomba.Turn_Left(0.5)
DesktopRoomba.Turn_Right(0.8)
DesktopRoomba.Forward(100)
sleep(2)
DesktopRoomba.Stop()
sleep(2)
DesktopRoomba.Backward(40)
sleep(2)
DesktopRoomba.Stop()
print("Power of the robot is ", DesktopRoomba.Power)
#DesktopRoomba.power()
