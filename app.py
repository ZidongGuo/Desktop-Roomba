import DesktopRoomba
from threading import Thread

DR=DesktopRoomba
DR.setup()
MinDistance=3 #all four read_distance() should return a value less than 3
MaxTime=800 #Read_IR_Reflectance() should return a value less than 800

def autonomy():
    while DR.power()==1:
