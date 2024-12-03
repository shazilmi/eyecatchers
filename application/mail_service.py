from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def daily_reminder_influencer(to):
	message = MIMEMultipart()
	message.attach(MIMEText("Greetings from Eyecatchers. We have noticed that you have a pending ad request which you have not yet responded to. This is just a reminder to login to your account if you would like to do so now."))
	message["To"] = to
	message["Subject"] = "Daily reminder regarding pending ad request"
	message["From"] = "eyecatchershead@gmail.com"
	client = SMTP(host = "localhost", port= "1025")
	client.send_message(msg = message)
	client.quit()
