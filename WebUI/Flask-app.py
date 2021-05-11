
import time
import DesktopRoomba
from threading import Thread
from time import sleep
#'from waiting import wait
import RPi.GPIO as GPIO
import random
DR=DesktopRoomba
DR.setup()
MinDistLR=8
MinDistF=10
MaxTime=800 #Read_IR_Reflectance() should return a value less than 800
Mode=-1
Stuck=0
IsOn=" "
IsOff="active"
IsMode0=" "
IsMode1=" "
from flask import Flask, redirect, render_template

app = Flask(__name__, static_folder='assets')

def FreeToGo():
    if (DR.Read_DistanceL()>MinDistLR and DR.Read_DistanceR()>MinDistLR and DR.Read_DistanceF()>MinDistF and DR.Power==1 and Stuck==0):
        return 1
    else:
        return 0

def Readytostart():
    if (DR.Power==1):
        return True
    return False

def RandAlgo():
    RandStart=time.time()
    MaxDuration1=600
    if (time.time()-RandStart >MaxDuration1):
        DR.Stop()
        DR.Power=0


    #wait(lambda: Readytostart())
    while (Mode==1 and DR.Power==1):
        while (FreeToGo()==1 and Mode==1):
            DR.Forward(40)
            sleep(0.03)
        if (Stuck==1):
            DR.Stop()
            sleep(0.5)
            DR.Backward(40)
            sleep(1)
            DR.Turn_Left(0.1)
            DR.Stop()
        while (DR.Read_DistanceF()<=MinDistF and Mode==1 and Stuck==0):
            if (DR.Power==0):
                DR.Stop()
                break
            DR.Stop()
            sleep(0.02)
            if (DR.Read_DistanceL()<MinDistLR and DR.Read_DistanceR()<MinDistLR):
                DR.Backward(40)
                sleep(1)
                RandAngle=3*random.random()
                DR.Turn_Right(RandAngle)
            elif (DR.Read_DistanceL()<MinDistLR):
                DR.Backward(40)
                sleep(0.3)
                RandAngle=2*random.random()
                DR.Turn_Right(RandAngle)
            else:
                DR.Backward(40)
                sleep
                RandAngle=2*random.random()
                DR.Turn_Left(RandAngle)
        while (DR.Read_DistanceL()<MinDistLR and DR.Read_DistanceF()>MinDistF  and Mode==1 and Stuck==0):
            if (DR.Power==0):
                DR.Stop()
                break

            RandAngle=random.random()
            DR.Turn_Right(RandAngle)
        while (DR.Read_DistanceR()<MinDistLR and DR.Read_DistanceF()>MinDistF  and Mode==1 and Stuck==0):
            if (DR.Power==0):
                DR.Stop()
                break

            RandAngle=random.random()
            DR.Turn_Left(RandAngle)

def SpiralAlgo():
    SpiralStart=time.time()
    MaxDuration0=1200
    if (time.time()-SpiralStart >MaxDuration0):
        DR.Stop()
        DR.Power=0
    while (Mode==0 and DR.Power==1):

        tourtime=2
        increasedtime=0.5
        numberofspiral=5
        minspeed=15
        maxspeed=70
        for i in range (0, numberofspiral):
            if (DR.Power==0 or Mode!=0):
                break

            cnt=0
            while (FreeToGo()==1 and cnt<1000):
                DR.pwm1.start(maxspeed)
                DR.pwm2.start(minspeed)
                GPIO.output(DR.Motor1A,GPIO.HIGH)
                GPIO.output(DR.Motor1B,GPIO.LOW)
                GPIO.output(DR.Motor1E,GPIO.HIGH)

                GPIO.output(DR.Motor2A,GPIO.HIGH)
                GPIO.output(DR.Motor2B,GPIO.LOW)
                GPIO.output(DR.Motor2E,GPIO.HIGH)
                sleep(tourtime/1000)
                cnt=cnt+1
            minspeed=minspeed+5
            tourtime=tourtime+increasedtime
            print("Spiral: ", i);
            if (FreeToGo()==0 and DR.Power==1):
                tourtime=2
                minspeed=15
                DR.Stop()
                sleep(1)
                if (Stuck==1):
                    DR.Backward(40)
                    RandTime=3*random.random()
                    sleep(RandTime)
                    DR.Stop()
                    break

                while (FreeToGo()==0 and Mode==0 and DR.Power==1 and Stuck==0):
                    DR.Stop()
                    sleep(0.5)
                    if (DR.Read_DistanceF()<=MinDistF and DR.Read_DistanceL()<MinDistLR and DR.Read_DistanceR()<MinDistLR):
                        DR.Back(40)
                        sleep(1)
                        RandAngle=3*random.random()
                        DR.Turn_Right(RandAngle)
                    elif (DR.Read_DistanceF()<=MinDistF-2):
                        RandAngle=2*random.random()
                        DR.Turn_Right(RandAngle)
                    elif (DR.Read_DistanceL() <MinDistLR-1):
                        RandAngle=random.random()
                        DR.Turn_Right(RandAngle)
                    elif (DR.Read_DistanceR() <MinDistLR-1):
                        RandAngle=random.random()
                        DR.Turn_Left(RandAngle)
                DR.Forward(50)
                RandTime=3*random.random()
                sleep(RandTime)
                break
            if (i==numberofspiral-1):
                tourtime=2
                minspeed=15
                maxspeed=70
                RandAngle=random.random()
                RandTime=3*random.random()
                DR.Turn_Left(RandAngle)
                DR.Forward(50)
                sleep(RandTime)
def GetStuck():
    global Stuck
    IMU=DR.Setup_IMU()
    while True:
        if DR.Power==1:
            Movement=1
            InitialTime=time.time()
            MaxTolerance=6
            while (time.time()-InitialTime < MaxTolerance and DR.Power==1):
                AngleAccel=DR.Read_Angle(IMU)
                Total=abs(AngleAccel[0]+AngleAccel[1]+AngleAccel[2])
                if Total>0.35:
                    #print("Not Stuck")
                    Movement=1
                    Stuck=0
                    break
                else:
                    Movement=0
            if Movement==0:
                Stuck=1
                print("Get Stuck")
@app.route("/")

def Home():
    return render_template('index.html',IsOff=IsOff,IsOn=IsOn, IsMode0=IsMode0, IsMode1=IsMode1)

@app.route('/power/<int:action>')
def SwitchPower(action):
    global IsOff
    global IsOn
    IsOff="active"
    IsOn=" "
    if action==0:
        IsOff="active"
        IsOn=" "
        DR.Stop()
        DR.Power=0
    elif action==1:
        IsOff=" "
        IsOn="active"
        t1=Thread(target=GetStuck)
        t1.start()
        DR.Power=1
    return redirect("/")

@app.route('/mode/<int:action>')
def SwitchMode(action):
    global Mode
    global IsMode0
    global IsMode1
    IsMode0=" "
    ISMode1=" "
    if action==0:
        IsMode0="active"
        IsMode1=" "
        Mode=0
        SpiralAlgo()
    elif action==1:
        IsMode0=" "
        IsMode1="active"
        Mode=1
        RandAlgo()
    return redirect("/")

if __name__ == "__main__":
    try:
        #t1=Thread(target=GetStuck)
        #t1.start()
        app.run(host='0.0.0.0', port=9876, debug=True, threaded=True)
        #t1.join()
    except KeyboardInterrupt:
        GPIO.cleanup()
