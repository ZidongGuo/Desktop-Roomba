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

from flask import Flask

app = Flask(__name__, static_folder='')
@app.route("/")

def Home():
    return app.send_static_file('index.html')

@app.route('/power/<int:action>')
def SwitchPower(action):
    if action==0:
        DR.Power=0
    elif action==1:
        DR.Power=1
    return redirect("/")

@app.route('/mode/<int:action>')
def SwitchMode(action):
    if action==0:
        Mode=0
    elif action==1:
        Mode=1
    return redirect("/")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
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
                    break
                while FreeToGo()==1:
                    if (DR.Power==0):
                        break
                    DR.Forward(40)
                    sleep(0.03)
                while (DR.Read_DistanceF()<=MinDistF):
                    if (DR.Power==0):
                        break
                    DR.Stop()
                    sleep(0.02)
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

    except KeyboardInterrupt:
        GPIO.cleanup()



