import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
aux = [2, 3, 14, 15, 18, 27, 23, 22]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)
GPIO.output(leds, 1)
while True:
    for i in range(8):
        GPIO.output(leds[i], GPIO.input(aux[i]))