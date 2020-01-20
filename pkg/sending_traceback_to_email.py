import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import os

with open('err.txt', 'r') as inp:
    MESSAGE = inp.readlines()

with open('data.txt', 'r') as inp:
    data = inp.read().split()

os.system('./clear_traceback.txt')

def send_email(MESSAGE):
    # create message object instance
    msg = MIMEMultipart()

    # setup the parameters of the message
    message = MESSAGE
    password = data[6]
    msg['From'] = data[5]
    msg['To'] = data[7]
    msg['Subject'] = '! ERROR TRACEBACK !'

    # add in the message body
    for stroke in MESSAGE:
        msg.attach(MIMEText(stroke, 'plain'))

    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)


    # send the message via the server.
    for item in range(1):
        server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("successfully sent email(-s) to " + msg['To'])

send_email(MESSAGE)
