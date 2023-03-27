import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT, initial = GPIO.HIGH)

p = GPIO.PWM(2, 1000)
p.start(0)

try:
    while True:
        DutCycle = int(input())
        p.ChangeDutyCycle(DutCycle)
        print('{:.4f}'.format(DutCycle * 3,3/100))
finally:
    GPIO.output(24, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()