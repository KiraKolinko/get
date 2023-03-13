import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, 0)
for i in range(10):
    GPIO.output(2, 1)
    time.sleep (0.5)
    GPIO.output(2, 0)
    time.sleep (0.5)
GPIO.cleanup()