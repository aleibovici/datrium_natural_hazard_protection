import smtplib
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import logging
import sys

logger = logging.getLogger()

# google is not allowing login via smtplib because
# it has flagged this type of login as "less secure",
# so what you have to do is go to this link while you're
# logged in to your google account, and allow the access:
# https://www.google.com/settings/security/lesssecureapps

''' Function to send email over secure STMP connection '''


def send_mail(smtp_server, port, sender_email, receiver_email, password, subject):

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    body = "Datrium Natural Hazart toolkit triggered an alert!"

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    text = message.as_string()

    context = ssl.create_default_context()  # Create a secure SSL context

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
    except:
        logger.error('Unexpected error: ' + str(sys.exc_info()[0]))
        pass
