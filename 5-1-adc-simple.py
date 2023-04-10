import RPi.GPIO as GPIO
import sys
from time import sleep
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def perevod(a):
    return[int(elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    for i in range(256):
        d = perevod(i)
        GPIO.output(dac, d)
        c = GPIO.input(comp)
        sleep(0.05)
        if c == 0:
            return i

try:
    while True:
        i = adc()
        if i != 0:
            print("{:.2f}v".format(3.3*i/256))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    
