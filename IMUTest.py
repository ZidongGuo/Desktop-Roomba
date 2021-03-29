import time
import board
import busio
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33

i2c = busio.I2C(board.SCL, board.SDA)

s33 = LSM6DS33(i2c)

while True:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(s33.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s"%(s33.gyro))
    print("")
    time.sleep(0.5)
