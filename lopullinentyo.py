import sys
import time
import random
import datetime
import telepot
import smtplib
import RPi.GPIO as GPIO


SMTP_SERVER = 'smtp.gmail.com' 
SMTP_PORT = 587 
GMAIL_USERNAME = 'ovikelloposti@gmail.com' 
GMAIL_PASSWORD = 'Oamk12345'


def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

GPIO.setup(23, GPIO.IN)


class Emailer:
    def sendmail(self, recipient, subject, content):
          
        #Headerit
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
  
        #Yhdistetaan Gmail Serveriin
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
  
        #Kirjaudutaan Gmailiin
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
  
        #Lahetetaan viesti ja poistutaan
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit
  
sender = Emailer()

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: %s') % command
    
    if command == 'on':
        sendTo = 'pyry.viirret@gmail.com'
        emailSubject = "Sinulla on vieraita!"
        emailContent = "Ovikelloa painettu klo: " + time.ctime()
        sender.sendmail(sendTo, emailSubject, emailContent)
        print("Email Sent")
        bot.sendMessage(chat_id, on(11))
    elif command =='off':
        bot.sendMessage(chat_id, off(11))


bot = telepot.Bot('1033039787:AAHuXy4ChYPSNfI0cTyPKfVUevHR3NNAnGQ')
bot.message_loop(handle)
print ('Kuunnellaan....')

while True:
    time.sleep(10)

