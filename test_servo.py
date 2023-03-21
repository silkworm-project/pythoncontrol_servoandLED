import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

servo1 = GPIO.PWM(17, 50) # GPIO 17 for PWM with 50Hz
servo2 = GPIO.PWM(18, 50) # GPIO 18 for PWM with 50Hz

servo1.start(0) # Initialization
servo2.start(0)

def set_angle(servo, angle):
    duty = angle / 18 + 2
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

try:
    while True:
        # Rotate servo1 from 0 to 180 degrees
        for angle in range(0, 180, 10):
            set_angle(servo1, angle)
        
        # Rotate servo2 from 0 to 180 degrees
        for angle in range(0, 180, 10):
            set_angle(servo2, angle)
            
except KeyboardInterrupt:
    servo1.stop()
    servo2.stop()
    GPIO.cleanup()

