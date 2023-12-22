from mqtt.mqttCon import run
import RPi.GPIO as GPIO

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        run()
    finally:
        GPIO.cleanup()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/