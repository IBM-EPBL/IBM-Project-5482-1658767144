import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RED = 18
AMBER = 23
GREEN = 24

GPIO.setup(RED , GPIO.OUT)
GPIO.setup(AMBER , GPIO.OUT)
GPIO.setup(GREEN , GPIO.OUT)

# Stop Function - Red light only
def Stop():
	global RED, AMBER, GREEN
	print("STOP")
	GPIO.output(RED , GPIO.HIGH)
	GPIO.output(AMBER, GPIO.LOW)
	GPIO.output(GREEN, GPIO.LOW)
	
# Get Ready to go Function - Red and amber lit
def GetReadyToGo():
	global RED, AMBER, GREEN
	print("Get Ready")
	GPIO.output(RED , GPIO.HIGH)
	GPIO.output(AMBER, GPIO.HIGH)
	GPIO.output(GREEN, GPIO.LOW)

# Go function - Green Only
def Go():
	global RED, AMBER, GREEN
	print("Go !")
	GPIO.output(RED , GPIO.LOW)
	GPIO.output(AMBER, GPIO.LOW)
	GPIO.output(GREEN, GPIO.HIGH)

# Get Ready To Stop function - Amber Only
def GetReadyToStop():
	global RED, AMBER, GREEN
	print("Warning lights changing")
	GPIO.output(RED , GPIO.LOW)
	GPIO.output(AMBER, GPIO.HIGH)
	GPIO.output(GREEN, GPIO.LOW)

# If ctrl-C is pressed then quit
try:
	while (True):
		# stop and pause between 3 and 5 seconds
		Stop();
		pauseTime = random.randint(3,5)
		time.sleep(pauseTime)	

		GetReadyToGo();
		time.sleep(1)	

		# go and pause between 3 and 5 seconds
		Go();
		pauseTime = random.randint(3,5)
		time.sleep(pauseTime)	

		GetReadyToStop();
		time.sleep(3)	

except KeyboardInterrupt:
	print("clean Up")
	GPIO.cleanup()
