import DesktopRoomba
from threading import Thread
from time import sleep
from waiting import wait
import RPi.GPIO as GPIO
import random
DR=DesktopRoomba
DR.setup()
MinDistLR=5 #all four read_distance() should return a value less than 3
MinDistF=7
MaxTime=800 #Read_IR_Reflectance() should return a value less than 800
Mode=1

def FreeToGo():
    if (DR.Read_DistanceL()>MinDistLR and DR.Read_DistanceR()>MinDistLR and DR.Read_DistanceF()>MinDistF and DR.Power==1):
        return 1
    else:
        return 0
def Readytostart():
    if (DR.Power==1):
        return True
    return False
try:
    while True:
        wait(lambda: Readytostart())

        while Mode==1:
            if (DR.Power==0):
                break;
            while FreeToGo()==1:
                DR.Forward(40)
            if (DR.Read_DistanceF()<=MinDistF):
                DR.Stop()
                if (DR.Read_DistanceL()<MinDistLR and DR.Read_DistanceR()<MinDistLR):
                    DR.Back(40)
                    sleep(0.2)
                    RandAngle=random.random()
                    DR.Turn_Right(RandAngle)
                elif (DR.Read_DistanceL()<MinDistLR):
                    RandAngle=random.random()
                    DR.Turn_Right(RandAngle)
                else:
                    RandAngle=random.random()
                    DR.Turn_Left(RandAngle)
            elif (DR.Read_DistanceL()<MinDistLR):
                RandAngle=random.random()
                DR.Turn_Right(RandAngle)
            elif (DR.Read_DistanceR()<MinDistLR):
                RandAngle=random.random()
                DR.Turn_Left(RandAngle)

except KeyboardInterrupt:
    GPIO.cleanup()

