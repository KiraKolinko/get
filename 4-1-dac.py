import RPi.GPIO as GPIO
import sys 
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def perevod(a, n):
    return[int(elem) for elem in bin(a)[2:].zfill(n)]
try:
    while(True):
        a = input("Введите число от 0 до 255 ")
        if a == 'q':
            sys.exit()    
        elif not a.isdigit() and ("-" not in a):
            print("Введенное значение не является числом!")
        elif int(a) < 0:
            print("Введенное значение отрицательно!")
        elif not a.isdigit() and int(a) % 1 != 0:
            print("Введенное значение не целое число!")
        elif int(a) > 255:
            print("Введенное значение больше допустимого!")
        else:
            GPIO.output(dac, perevod(int(a), 8))
            print('{:.4f}'.format(int(a) / 256 * 3,3))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()