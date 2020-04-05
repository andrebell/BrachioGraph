import RPi.GPIO as GPIO
import time

GPIO_green = 4
GPIO_red = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_green, GPIO.OUT)
GPIO.setup(GPIO_red, GPIO.OUT)

green = 1
red = 0

for i in range(100):
    GPIO.output(GPIO_green, green)
    GPIO.output(GPIO_red, red)

    green, red = red, green

    time.sleep(0.3)

GPIO.cleanup()

