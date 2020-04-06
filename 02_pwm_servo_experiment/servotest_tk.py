from tkinter import *

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)

pwm = GPIO.PWM(14, 50)
pwm.start(0)

def SetAngle(angle):
    angle=float(angle)
    max_duty = 11.4 # Maximum duty cycle for the left-most position
    min_duty = 2.7 # Minimum duty cycle for the right-most position
    duty = (max_duty - min_duty) / 180 * angle + min_duty
    GPIO.output(14, True)
    pwm.ChangeDutyCycle(duty)

root = Tk()
root.title("Set servo angle")
angle_slider = Scale(root, from_=0, to=180, orient=HORIZONTAL, command=SetAngle)
angle_slider.set(0)
angle_slider.pack()
mainloop()

GPIO.cleanup()
