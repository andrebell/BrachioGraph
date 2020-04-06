import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)

pwm = GPIO.PWM(14, 50)

pwm.start(0)

def SetAngle(angle):
    max_duty = 11.4 # Maximum duty cycle for the left-most position
    min_duty = 2.7 # Minimum duty cycle for the right-most position
    duty = (max_duty - min_duty) / 180 * angle + min_duty
    GPIO.output(14, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(14, False)
    pwm.ChangeDutyCycle(0)

#SetAngle(0)

for i in range(5):
    SetAngle(0)
    SetAngle(90)
    SetAngle(180)
    SetAngle(90)

GPIO.cleanup()
