import smtplib
from email.message import EmailMessage

def sendmail(to,subject,body):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('likhitha1137@gmail.com','jamj cvyz keqa lylw')
    msg = EmailMessage()
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()

sendmail('hemavaniy58@gmail.com','hi this is Likhitha','Ur are from GEC how was the class going?')
print('mailsended')