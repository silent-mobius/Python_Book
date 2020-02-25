#!/usr/bin/env python3

import smtplib

sender = 'from@virusdomain.com'
receivers = ['alex@vaiolabs.com']

message = """From: From hacker <from@fromdomain.com>
To: To Lior <to@todomain.com>
Subject: SMTP virus mail

This is a virus e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except:
   print("Error: unable to send email")
