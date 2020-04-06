from tkinter import *

import RPi.GPIO as GPIO
import time

GPIO_green = 4
GPIO_red = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_green, GPIO.OUT)
GPIO.output(GPIO_green, 0)

GPIO.setup(GPIO_red, GPIO.OUT)
GPIO.output(GPIO_red, 0)

def toggle_green():
    GPIO.output(GPIO_green, 1-GPIO.input(GPIO_green))

def toggle_red():
    GPIO.output(GPIO_red, 1-GPIO.input(GPIO_red))

root = Tk()
root.title("Toggle LEDs")
Button(root, text="Grün umschalten", width=15, command=toggle_green).pack()
Button(root, text="Rot umschalten", width=15, command=toggle_red).pack()
mainloop()

GPIO.cleanup()


