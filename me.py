##########################################################################################################
##########################################################################################################
###################################   Kurtis Hall 14019369 Project   #####################################
##########################################################################################################
##########################################################################################################

#Multiple Imports
import RPi.GPIO as GPIO
import time
from Adafruit_PWM_Servo_Driver import PWM
from sgh_PCF8591P import sgh_PCF8591P

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN) #Right IR set to 11
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Front activates
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Left IR set to 7

GPIO.setup(26,GPIO.OUT) #Left forward motor
GPIO.setup(24,GPIO.OUT) #Left reverse motor
GPIO.setup(19,GPIO.OUT) #Right forward motor
GPIO.setup(21,GPIO.OUT) #Right reverse motor

GPIO.setup(26, GPIO.OUT)
LF = GPIO.PWM(26, 20)#sets amount of power
LF.start(0)

GPIO.setup(24, GPIO.OUT)
LR = GPIO.PWM(24, 20)#sets amount of power
LR.start(0)

GPIO.setup(19, GPIO.OUT)
RF = GPIO.PWM(19, 20)#sets amount of power
RF.start(0)

GPIO.setup(21, GPIO.OUT)
RR = GPIO.PWM(21, 20)#sets amount of power
RR.start(0)

speed = 100#set speed

flag=0
while True:
	j=GPIO.input(13)
	if j==1: #Robot is activated when button is pressed
		flag=1
		print "Robot Activated",j
	
	while flag==1:
		i=GPIO.input(7) 
		k=GPIO.input(11)
		if i==0: 
			print "Right Side Detected!",i 
			#Reverse
    			LF.ChangeDutyCycle(0)
    			LR.ChangeDutyCycle(speed)
    			RF.ChangeDutyCycle(0)
    			RR.ChangeDutyCycle(speed)
    			LR.ChangeFrequency(speed + 5)
    			RR.ChangeFrequency(speed + 5)
			#Turns Left
    			LF.ChangeDutyCycle(0)
   			LR.ChangeDutyCycle(speed)
   			RF.ChangeDutyCycle(speed)
    			RR.ChangeDutyCycle(0)
    			LR.ChangeFrequency(speed + 5)
    			RF.ChangeFrequency(speed + 5)


		if k==0: #Left IR 
			print "Left Side Detected",k
			#Reverse
    			LF.ChangeDutyCycle(0)
    			LR.ChangeDutyCycle(speed)
    			RF.ChangeDutyCycle(0)
    			RR.ChangeDutyCycle(speed)
    			LR.ChangeFrequency(speed + 5)
    			RR.ChangeFrequency(speed + 5)
			#Turns Right
    			LF.ChangeDutyCycle(speed)
    			LR.ChangeDutyCycle(0)
    			RF.ChangeDutyCycle(0)
    			RR.ChangeDutyCycle(speed)
    			LF.ChangeFrequency(speed + 5)
    			RR.ChangeFrequency(speed + 5)
		elif i==0 and k==0:
			print "Left and Right Detected!!"
			#Reverse
    			LF.ChangeDutyCycle(0)
    			LR.ChangeDutyCycle(speed)
    			RF.ChangeDutyCycle(0)
    			RR.ChangeDutyCycle(speed)
    			LR.ChangeFrequency(speed + 5)
    			RR.ChangeFrequency(speed + 5)
			#Turns Right
    			LF.ChangeDutyCycle(speed)
    			LR.ChangeDutyCycle(0)
    			RF.ChangeDutyCycle(0)
    			RR.ChangeDutyCycle(speed)
    			LF.ChangeFrequency(speed + 5)
    			RR.ChangeFrequency(speed + 5)
			time(4)
		elif i==1 and k==1:
			print "Clear Route",i
			#Forward
    			LF.ChangeDutyCycle(speed)
    			LR.ChangeDutyCycle(0)
    			RF.ChangeDutyCycle(speed)
    			RR.ChangeDutyCycle(0)
    			LF.ChangeFrequency(speed + 5)
    			RF.ChangeFrequency(speed + 5)
		j=GPIO.input(13)
		if j==1: 
			flag=0
			print "Terminated!",j
			#Stops
    			LF.ChangeDutyCycle(0)
    			LR.ChangeDutyCycle(0)
    			RF.ChangeDutyCycle(0)
    			RR.ChangeDutyCycle(0)
			
##########################################################################################################
#						The END!					         #
##########################################################################################################			
