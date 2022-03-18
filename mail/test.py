import smtplib
import ssl
from credentials import password, sender_email

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
# sender_email = "eglootz.code@gmail.com"  # Enter your address
receiver_email = "elias.glootz@gmail.com"  # Enter receiver address
# password = "Hagridfan06!"  # input("Type your password and press enter: ")
message = """\
Subject: Deine Mom

Das ist eine Test-Nachricht!"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
