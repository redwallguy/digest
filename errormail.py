import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from secrets import pyErrorsPass
 
def sendDevError(mail_subject, mail_msg):
    fromaddr = "redwallguy.python.errors@gmail.com"
    toaddr = "redwallguy@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = mail_subject
 
    body = mail_msg
    msg.attach(MIMEText(body, 'plain'))
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr,pyErrorsPass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
