import smtplib
import ssl
import imghdr
from email.message import EmailMessage
from credentials import password, sender_email, receiver_email

port = 465  # For SSL
smtp_server = "smtp.gmail.com"

context = ssl.create_default_context()


def send_mail(subject, content, person):
    message = f"""\
        {person}
Subject: {subject}

{content}"""
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
