import RPi.GPIO as GPIO
import time

# Pin Definitions
output_pin = 18  # BOARD pin 12, BCM pin 18
list_pin = [18, 23, 24, 25, 8, 7]

def main():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BCM)
    # set pin as an output
    for pin in list_pin:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        
    try:
        while True:
            time.sleep(1)
            for pin in list_pin:
                GPIO.output(pin, GPIO.HIGH)
            time.sleep(1)
            for pin in list_pin:
                GPIO.output(pin, GPIO.LOW)
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()