import DesktopRoomba
from time import sleep
DesktopRoomba.setup()

DesktopRoomba.Read_Ultrasonic_Distance()

DesktopRoomba.Read_IR_Reflectance()

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


