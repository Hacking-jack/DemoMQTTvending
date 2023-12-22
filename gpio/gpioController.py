import RPi.GPIO as GPIO
import time


def activa(msg: str):
    # Set the GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Set up GPIO pin 17 as an output
    GPIO.setup(21, GPIO.OUT)

    if (msg == "ON"):
        GPIO.output(21, GPIO.HIGH)
        time.sleep(1.5)
        GPIO.output(21, GPIO.LOW)
        time.sleep(1)
