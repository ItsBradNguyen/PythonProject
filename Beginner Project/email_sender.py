# Importing Libraries
from email.message import EmailMessage
import ssl
import smtplib

# Python App Password: kzbacvhoyihbzvkv

# Defining Variables
email_sender = 'brad.nguyen2512@gmail.com'
email_password = 'kzbacvhoyihbzvkv'

# User Input
email_receiver = input("Who do you want to send the email to? ").lower()
subject = input('What do you want the subject to be? ')
body = input('Please enter the body of the message: ')

# Class Inference
em = EmailMessage()
em['From']= email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())