import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
GPIO_ir =1
try:

  while True:

    GPIO.setup(GPIO_ir,GPIO.OUT)
    GPIO.output(GPIO_ir, GPIO.HIGH)
    time.sleep(1) 
    GPIO.setup(GPIO_ir,GPIO.IN)
    start=time.time()
    GPIO.wait_for_edge(GPIO_ir, GPIO.FALLING)
    end=time.time()
    print("%f seconds, %f us" %(end-start,1000000*(end-start) ) )

except KeyboardInterrupt:
  GPIO.cleanup()
  sys.exit()
