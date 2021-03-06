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
Mode=2

def FreeToGo():
    if (DR.Read_DistanceL()>MinDistLR and DR.Read_DistanceR()>MinDistLR and DR.Read_DistanceF()>MinDistF and DR.Power==1):
        return 1
    else:
        return 0
DR.Power=1
def Readytostart():
    if (DR.Power==1):
        return True
    return False

try:
    while True:
        wait(lambda: Readytostart())

        while Mode==1:
            if (DR.Power==0):
                break
            while FreeToGo()==1:
                DR.Forward(40)
                sleep(0.03)
            while (DR.Read_DistanceF()<=MinDistF):
                if (DR.Power==0):
                    break
                DR.Stop()
                sleep(0.02)
                if (DR.Read_DistanceL()<MinDistLR and DR.Read_DistanceR()<MinDistLR):
                    DR.Backward(40)
                    sleep(0.5)
                    RandAngle=random.random()
                    DR.Turn_Right(RandAngle)
                elif (DR.Read_DistanceL()<MinDistLR):
                    RandAngle=random.random()
                    DR.Turn_Right(RandAngle)
                else:
                    RandAngle=random.random()
                    DR.Turn_Left(RandAngle)
            while (DR.Read_DistanceL()<MinDistLR and DR.Read_DistanceF()>MinDistF):
                if (DR.Power==0):
                    break

                RandAngle=random.random()
                DR.Turn_Right(RandAngle)
            while (DR.Read_DistanceR()<MinDistLR and DR.Read_DistanceF()>MinDistF):
                if (DR.Power==0):
                    break

                RandAngle=random.random()
                DR.Turn_Left(RandAngle)
        while Mode==2:
            if (DR.Power==0):
                break

            tourtime=3
            increasedtime=0.5
            numberofspiral=10
            minspeed=30
            maxspeed=90
            for i in range (0, numberofspiral):
                if (DR.Power==0):
                    break
                if (FreeToGo()==0):
                    while (FreeToGo()==0):
                        DR.Stop()
                        sleep(0.5)
                        if (DR.Read_DistanceF()<=MinDistF and DR.Read_DistanceL()<MinDistLR and DR.Read_DistanceR()<MinDistLR):
                            DR.Back(40)
                            sleep(0.5)
                        RandAngle=random.random()
                        DR.Turn_Right(RandAngle)
                    DR.Forward(50)
                    RandTime=3*random.random()
                    sleep(RandTime)
                    break
                DR.pwm1.start(maxspeed)
                DR.pwm2.start(minspeed)
                GPIO.output(DR.Motor1A,GPIO.HIGH)
                GPIO.output(DR.Motor1B,GPIO.LOW)
                GPIO.output(DR.Motor1E,GPIO.HIGH)

                GPIO.output(DR.Motor2A,GPIO.HIGH)
                GPIO.output(DR.Motor2B,GPIO.LOW)
                GPIO.output(DR.Motor2E,GPIO.HIGH)
                sleep(tourtime)
                minspeed=minspeed+5
                tourtime=tourtime+increasedtime
                print("Spiral: ", i);
except KeyboardInterrupt:
    GPIO.cleanup()
