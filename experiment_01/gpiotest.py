import RPi.GPIO as GPIO
import time

GPIO_green = 4
GPIO_red = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_green, GPIO.OUT)
GPIO.setup(GPIO_red, GPIO.OUT)

def blinke(n):
    for i in range(n):
        GPIO.output(GPIO_green, 0)
        GPIO.output(GPIO_red, 0)

        time.sleep(0.3)

        GPIO.output(GPIO_green, 1)
        GPIO.output(GPIO_red, 1)

        time.sleep(0.3)

blinke(10)

GPIO.cleanup()

