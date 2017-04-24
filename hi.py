##########################################################################################################
##########################################################################################################
###################################   Kurtis Hall 14019369 Project   #####################################
##########################################################################################################
##########################################################################################################

#Multiple imports
import os
import time
from SimpleCV import *
import smtplib
from datetime import datetime as dt
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

IMG = Camera()#Camera is intiated.
fmt = "%Y-%m-%d %H-%M-%S"#Date,Month,Year,Hour,Minute,Seconds
Time = 10#Time it takes to send the email
Stime = time.time()
path = "Photo" #Directory 
if not os.path.exists("Photo"):
	os.makedirs("Photo")


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

	
while True:#While loop which grabs images until it is told to stop.

        settime = time.time()
        PIC1 = IMG.getImage().toGray()
	time.sleep(0.1)#waits before taking next photo(darker image)
	
	PIC = IMG.getImage()
        PIC2 = IMG.getImage().toGray()
	time.sleep(1)
        d = (PIC1 - PIC2).binarize().invert()

        matrix = d.getNumpy()
        avg = matrix.mean()
	blobs = d.findBlobs()
	
	if settime >= (Stime + Time):

		for root, dirs, files in os.walk(path):#checks the folder for images
			for file in files:#finds the image
				Sortfile = sorted(files)[0]
				mailer = os.path.join(root, Sortfile)
				email(mailer)#sends image to email function
				
				
	if avg >= 10:#average mean greater equal to 10

		if blobs:

			for b in blobs:
				try:
					PIC.drawCircle((b.x,b.y),b.radius(),SimpleCV.Color.GREEN,3)#draws green circle around object
				except:
					e = sys.exc_info()[0]
					
					
					

		name = dt.now().strftime(fmt) # filename using date, month, time
		
		
		i = 1 #counter
		PIC.save("Photo/Intruder%s-%s.png" % (name, i))#saves file with intruder and the date
		print("Initiating Camera!")#prints to command line

##########################################################################################################
#						The END!					         #
##########################################################################################################
