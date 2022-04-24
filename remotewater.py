import RPi.GPIO as GPIO



transmitter = 17

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(transmitter, GPIO.OUT)

while True:
    GPIO.output(transmitter, GPIO.HIGH)