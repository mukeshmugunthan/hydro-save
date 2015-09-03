import sys
       import RPi.GPIO as GPIO

       # Identify which pin controls transistormotor_pin = 4
       # Set pin 4 as output
 	GPIO.setmode(GPIO.BCM)
	GPIO.setup(motor_pin, GPIO.OUT)
	# Get what action to take
	action = sys.argv.pop()
	if action == "on" :
	print "Turning motor on"
	GPIO.output(motor_pin, GPIO.HIGH)
	elif action == "off" :
	print "Turning motor off"
	GPIO.output(motor_pin, GPIO.LOW)
	else :
	 print "will let yu know"
