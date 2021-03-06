##########################################################################################################
##########################################################################################################
###################################   Kurtis Hall 14019369 Project   #####################################
##########################################################################################################
##########################################################################################################
#!/usr/bin/python
#Multiple imports

import SimpleCV
import os
import time
import smtplib
import numpy as np
import uuid
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



##########################################################################################################
#				Sending Attached PNG files to recipient.			         #
##########################################################################################################

def email(Gmail):

	img_data = open(Gmail, 'rb').read()
        msg = MIMEMultipart('mixed')
        msg['Subject'] = 'Important Message!'#subject title
        msg['From'] = 'kurtax.h1@googlemail.com'
        msg['Reply-to'] = ', '.join('kurtax.h1@googlemail.com')
        text = MIMEText("Intruder has been spotted!")#email body text
        msg.attach(text)#attach body text
        image = MIMEImage(img_data, name=os.path.basename(Gmail))
        msg.attach(image)#attaches img

        s = smtplib.SMTP('smtp.gmail.com', 587)#SMTP server connection
        s.ehlo()
        s.starttls()#Starts transport layer security
        s.ehlo#Extended hello command
        s.login('kurtax.h1@googlemail.com', 'kurtax%1')#Login Details
        s.sendmail('kurtax.h1@googlemail.com','kurtax.h1@googlemail.com', msg.as_string())#Sending email
        s.close()#Closes
	
##########################################################################################################
#					SimpleCV Object detection.				         #
##########################################################################################################

cam = Camera(prop_set={"width":300,"height":300})

		  
threshold = 5.0
		  #Threshold set to 

Time = 10 #Time it takes to send the email

Stime = time.time()

path = "Photo" #Directory 
if not os.path.exists("Photo"):
	os.makedirs("Photo")

while True:#While loop which grabs images until it is told to stop.

        settime = time.time()

        img01 = cam.getImage().toGray()

        time.sleep(0.5)

	original = cam.getImage()

        img02 = cam.getImage().toGray()

        diff = (img01 - img02).binarize(50).invert()
	diff.show()

        matrix = diff.getNumpy()
        mean = matrix.mean()


	blobs = diff.findBlobs()

	if settime >= (Stime + Time):

		for root, dirs, files in os.walk(path):#checks the folder for images
			for file in files:#finds the image
				Sortfile = sorted(files)[0]
				mailer = os.path.join(root, Sortfile)
				email(mailer)#sends image to email function

				
				
	if mean >= threshold:


		if blobs:

			for b in blobs:
				try:
					loc = (b.x,b.y) 
					original.drawCircle(loc,b.radius(),Color.RED,2)
				except:
					e = sys.exc_info()[0]
					
					
					
		#use the current date to create a unique file name
		timestr = time.strftime("%Y%m%d-%H%M%S")
		
		#initialize the counter variable
		i = 1
		
		#check to see if the filename already exists
		while os.path.exists("Photo/motion%s-%s.png" % (timestr, i)):
			#if it does, add one to the filename and try again
			i += 1
		#once a unique filename has been found, save the image
		original.save("Photo/motion%s-%s.png" % (timestr, i))
		
		print("Motion Detected")
##########################################################################################################
#						The END!					         #
##########################################################################################################
