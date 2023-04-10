import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def perevod(a):
    return[int(elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k = [0 for i in range(8)]
    for i in range(8):
        k_k = k.copy()
        k_k[i] = 1
        GPIO.output(dac, k_k)
        sleep(0.05)
        if GPIO.input(comp) == 1:
            k = k_k
    n = ''.join([str(i) for i in k])
    return int(n, 2)
try:
    while True:
        k = adc()
        if k != 0:
            print(k, "{0:.2f}B".format(int(k)/255 * 3.3))
        GPIO.output(dac, perevod(k))

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()