import DesktopRoomba
from threading import Thread
from time import sleep
import RPi.GPIO as GPIO
import random
DR=DesktopRoomba
DR.setup()
#MinDistLR=5 #all four read_distance() should return a value less than 3
MinDistF=7
#MaxTime=800 #Read_IR_Reflectance() should return a value less than 800
#Mode=1
#DR.Power=1
DR=DesktopRoomba
MinDistF=7
while True:
        DR.Read_DistanceF()
        sleep(0.03)
        #if (DR.Read_DistanceF()<=MinDistF):
        #    DR.Stop()
        #    if (DR.Read_DistanceL()<MinDistLR and DR.Read_DistanceR()<MinDistLR):
        #        DR.Back(40)
        #        sleep(0.2)
        #        andAngle=random.random()
        #        DR.Turn_Right(RandAngle)
        #    elif (DR.Read_DistanceL()<MinDistLR):
        #        RandAngle=random.random()
        #        DR.Turn_Right(RandAngle)
        #    else:
        #        RandAngle=random.random()
        #        DR.Turn_Left(RandAngle)
