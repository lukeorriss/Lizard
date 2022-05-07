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

# Main Routine
def timeElapsed(seconds):
    return str(datetime.timedelta(seconds=seconds))
def timeLeft(seconds):
    interval = 43200
    time_left = interval - seconds
    return str(datetime.timedelta(seconds=time_left))
running = True
def main():

    time_elapsed = 0
    total_runtime = 0 
    while running:
        os.system("clear")

        if time_elapsed < 5:
            #GPIO.output(pump, GPIO.HIGH)
            print("Watering")
            # lcd.setRGB(60,248,248);
            lcd.setRGB(255,0,0)
            lcd.setCursor(0, 0)
            lcd.printout("Watering...                 ")
        else:
            GPIO.output(pump, GPIO.LOW)


        if time_elapsed > 5:
            exit();

        # Print to Terminal
        print("L " + timeLeft(time_elapsed) + "      ")
        print("E " + timeElapsed(total_runtime) + "      ")
        
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        # Print to Display
        # lcd.setRGB(248,248,60)
        lcd.setRGB(255,0,0)
        lcd.setCursor(0, 0)
        lcd.printout("Last Watered                 ")
        lcd.setCursor(0, 1)
        lcd.printout(dt_string + "                 ")
        
        # Iterate Timers
        time_elapsed = time_elapsed + 1
        total_runtime = total_runtime + 1
        time.sleep(1)


main()




