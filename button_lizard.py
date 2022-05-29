import time
import os
import RGB1602
import RPi.GPIO as GPIO
import datetime

# Initialise Screen
lcd = RGB1602.RGB1602(16,2)

# Initialise Pump
pump = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pump, GPIO.OUT)

# Initialise Button
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Main Routine
def timeElapsed(seconds):
    return str(datetime.timedelta(seconds=seconds))
def timeLeft(seconds):
    interval = 43200
    time_left = interval - seconds
    return str(datetime.timedelta(seconds=time_left))

def retry():
    main()
def main():
    lcd.setCursor(0, 0)
    lcd.printout("Script Started            ")
    time.sleep(3)
    try:
        while True:
            input_sate = GPIO.input(5)
            
            if input_sate == False:

                GPIO.output(pump, GPIO.HIGH)
                print("Watering")
                # lcd.setRGB(60,248,248);
                lcd.setRGB(255,0,0)
                lcd.setCursor(0, 0)
                lcd.printout("Watering...                 ")
                time.sleep(8)

                GPIO.output(pump, GPIO.LOW)

                now = datetime.datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                # Print to Display
                # lcd.setRGB(248,248,60)
                lcd.setCursor(0, 0)
                lcd.printout("Last Watered:                ")
                lcd.setCursor(0, 1)
                lcd.printout(dt_string + "                 ")
    except OSError as e:
        lcd.setRGB(255,0,0)
        lcd.setCursor(0, 0)
        lcd.printout("Error: OSError           ")
        lcd.setCursor(0, 1)
        lcd.printout("Restarting...")
        retry();
main()




